# Load necessary libraries
library(httr)
library(jsonlite)
library(dplyr)
library(readxl)
library(ggplot2)
library(dplyr)
library(stringr)

get_detailed_clicks <- function(link, token) {
  base_url <- "https://api-ssl.bitly.com/v4/bitlinks/"
  link_id <- sub("https://", "", link)
  bitly_url <- paste0(base_url, link_id, "/clicks")
  
  response <- GET(bitly_url, 
                  add_headers(Authorization = paste("Bearer", token)),
                  query = list(unit = "day", units = -1))  # Get all available data
  
  if (status_code(response) != 200) {
    print(paste("Error for link:", link, "Status code:", status_code(response)))
    return(data.frame(Link = link, total_clicks = 0, date = as.Date(NA), clicks = 0))
  }
  
  response_json <- fromJSON(content(response, "text"), flatten = TRUE)
  
  if (length(response_json$link_clicks) > 0) {
    clicks_df <- as.data.frame(response_json$link_clicks)
    clicks_df$Link <- link
    clicks_df$date <- as.Date(clicks_df$date)
    clicks_df$total_clicks <- sum(clicks_df$clicks)
    return(clicks_df)
  }
  
  return(data.frame(Link = link, total_clicks = 0, date = as.Date(NA), clicks = 0))
}

# Function to handle rate-limited API calls
get_click_data_with_throttling <- function(link, token) {
  Sys.sleep(0.5)  # Sleep for 0.5 seconds between requests
  return(get_detailed_clicks(link, token))
}

# Your Bit.ly API token
bitly_token <- "cf0f12b521bd873f4ac558e366cc946b456ef90d"

# Read the CSV file
data <- read.csv('email-launch.csv', header = TRUE)

# Filter data to only include rows where sent == 1
data <- data[data$sent == 1, ]

# Ensure no duplicate rows in the filtered data
data <- data %>% distinct() 

# Extract links from the filtered data
links <- unique(data$Link)  # Ensuring unique links

# Get detailed click data for all unique links with throttling
detailed_click_data_list <- lapply(links, get_click_data_with_throttling, token = bitly_token)

# Combine all detailed click data into a single dataframe
detailed_click_data_df <- bind_rows(detailed_click_data_list)

# Calculate summary click data
summary_click_data <- detailed_click_data_df %>%
  group_by(Link) %>%
  summarize(
    total_clicks = sum(clicks, na.rm = TRUE),
    clicked = as.integer(sum(clicks, na.rm = TRUE) > 0)
  )

# Merge the summary data back to the original dataframe
data <- data %>%
  left_join(summary_click_data, by = "Link") %>%
  mutate(
    total_clicks = coalesce(total_clicks, 0),
    clicked = coalesce(clicked, 0)
  )

# Add detailed click data (if any) to the main dataframe
data <- data %>%
  left_join(detailed_click_data_df %>% 
              filter(clicks > 0) %>% 
              select(Link, date, clicks),
            by = "Link") %>%
  mutate(
    clicks = coalesce(clicks, 0),
    date = if_else(is.na(date) & total_clicks == 0, as.Date(NA), date)
  )

# Display the entire dataframe
print(data)

# Display summary statistics
summary(data)

# View the updated dataframe
print(head(data))

# Display combined click summary data
print(summary_click_data)

# Show distribution of clicks over time
ggplot(detailed_click_data_df %>% filter(clicks > 0), aes(x = date, y = clicks)) +
  geom_line() +
  labs(title = "Clicks Over Time", x = "Date", y = "Number of Clicks")

# Table of clicked vs not clicked
table(data$clicked)

# Export the data
#write.csv(data, 'email-launch-detailed-clicks.csv', row.names = FALSE)


d1 <- data |> 
  dplyr::select(contact_email, department, condition, clicked, date) |> 
  group_by(contact_email) |>
  mutate(
    earliest_click = if(any(clicked == 1, na.rm = TRUE)) min(date[clicked == 1], na.rm = TRUE) else as.Date(NA),
    clicked = case_when(
      is.na(earliest_click) ~ 0,
      earliest_click < as.Date("2024-07-07") ~ 1,
      TRUE ~ 0
    )
  ) |>
  ungroup() |>
  select(-earliest_click)|> 
  select(contact_email, condition, department, clicked) |> 
  unique()




# First, let's count the number of logins for each email in all_surveys
login_counts <- all_surveys %>%
  group_by(contact_email) %>%
  summarise(logins = n())

# Now, let's join this with the original data and create our variables
result <- d1 %>%
  left_join(login_counts, by = "contact_email") %>%
  mutate(
    login = ifelse(is.na(logins), 0, 1),  # Binary login indicator
    logins = ifelse(is.na(logins), 0, logins)  # Continuous login count
  ) %>%
  mutate(
    university = str_replace(department, "-.*$", ""),
    discipline = case_when(
      str_detect(department, "Mathematics$") ~ "Mathematics",
      str_detect(department, "Physics$") ~ "Physics",
      str_detect(department, "Computer Science$") ~ "Computer Science",
      str_detect(department, "Chemistry$") ~ "Chemistry",
      str_detect(department, "Mechanical Engineering$") ~ "Mechanical Engineering",
      TRUE ~ NA_character_
    )
  ) %>%
  select(contact_email, condition, clicked, login, logins, university, discipline, everything())

# View the result
print(head(result, 10))

summary(lm(login ~ condition, data=result))

table(result$clicked)/nrow(result)

table(d1$clicked)
