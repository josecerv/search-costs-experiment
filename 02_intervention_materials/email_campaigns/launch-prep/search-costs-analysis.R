# Load necessary libraries
library(httr)
library(jsonlite)
library(dplyr)
library(readr)
library(readxl)
library(lubridate)
library(purrr)
library(stringr)
library(tidyr)
library(ggplot2)
library(qualtRics)
library(patchwork)
library(RColorBrewer)
library(gridExtra)
library(ggpattern)
library(ggtext)

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

# Function to read all Excel files from a folder
read_excel_files <- function(folder) {
  files <- list.files(folder, pattern = "*.xlsx", full.names = TRUE)
  data <- map_df(files, ~read_excel(.x) %>% 
                   mutate(batch = str_extract(basename(.x), "batch\\d+"),
                          send_date = as.Date(str_extract(basename(.x), "\\d{8}"), format = "%Y%m%d"),
                          time = "Time 1"))
  return(data)
}

# Function to read all CSV files from a folder
read_csv_files <- function(folder) {
  files <- list.files(folder, pattern = "*.csv", full.names = TRUE)
  data <- map_df(files, ~read_csv(.x) %>% 
                   mutate(batch = str_extract(basename(.x), "batch\\d+"),
                          send_date = as.Date(str_extract(basename(.x), "\\d{8}"), format = "%Y%m%d"),
                          time = "Time 2"))
  return(data)
}

# Read and combine all files
data_send_one <- read_excel_files("send-one")
data_send_two <- read_csv_files("send-two")

# Combine data and pivot to wide format
consolidated_data <- bind_rows(data_send_one, data_send_two) %>%
  pivot_wider(
    id_cols = c(contact_email, department, condition),
    names_from = time,
    values_from = c(link_key, Link, batch, send_date),
    names_sep = "_"
  )

# consolidated_data <- consolidated_data[1:100,]

# Your Bit.ly API token
bitly_token <- "cf0f12b521bd873f4ac558e366cc946b456ef90d"

# Make sure the get_click_data_with_throttling function is defined
get_click_data_with_throttling <- function(link, token) {
  Sys.sleep(0.5)  # Sleep for 0.5 seconds between requests
  return(get_detailed_clicks(link, token))
}

# Get click data for all links
get_click_data <- function(link, token) {
  click_info <- get_click_data_with_throttling(link, token)
  if(is.data.frame(click_info)) {
    return(click_info)
  } else {
    return(data.frame(date = as.Date(NA), clicks = 0, total_clicks = 0))
  }
}

# Function to combine columns, preferring non-NA values
combine_columns <- function(col1, col2) {
  ifelse(!is.na(col1), col1, col2)
}

# Consolidate the data
consolidated_data <- consolidated_data %>%
  mutate(
    link_key = combine_columns(`link_key_Time 1`, `link_key_Time 2`),
    Link = combine_columns(`Link_Time 1`, `Link_Time 2`)
  ) %>%
  select(-`link_key_Time 1`, -`link_key_Time 2`, -`Link_Time 1`, -`Link_Time 2`)

# Get unique links
all_links <- consolidated_data$Link %>% 
  unique() %>% 
  na.omit()

# Create a dataframe of all unique links
link_df <- data.frame(Link = all_links)

# Fetch click data for all unique links
all_click_data <- link_df %>%
  mutate(click_info = map(Link, ~get_click_data(.x, bitly_token))) %>%
  unnest(click_info, names_repair = "unique")

# First, let's clean up all_click_data
all_click_data <- all_click_data %>%
  rename(Link = Link...1) %>%
  select(-Link...4)  # Remove the duplicate Link column

# Function to calculate clicks within a specific date range
calculate_clicks <- function(link, start_date, end_date, all_click_data) {
  if (is.na(link) || is.na(start_date)) {
    return(list(num_clicks = 0, binary_click = 0))
  }
  
  all_click_data %>%
    filter(Link == link, date >= start_date & date <= end_date) %>%
    summarise(num_clicks = sum(clicks, na.rm = TRUE),
              binary_click = as.integer(sum(clicks, na.rm = TRUE) > 0),
              .groups = "drop")
}

# Calculate click data for each participant
final_data <- consolidated_data %>%
  rowwise() %>%
  mutate(
    clicks_t1 = list(calculate_clicks(Link, `send_date_Time 1`, `send_date_Time 1` + days(14), all_click_data)),
    clicks_t2 = list(calculate_clicks(Link, `send_date_Time 2`, `send_date_Time 2` + days(14), all_click_data))
  ) %>%
  mutate(
    binary_click_t1 = clicks_t1$binary_click,
    num_clicks_t1 = clicks_t1$num_clicks,
    binary_click_t2 = clicks_t2$binary_click,
    num_clicks_t2 = clicks_t2$num_clicks,
    binary_click_all = as.integer(binary_click_t1 | binary_click_t2),  # Use logical OR
    num_clicks_all = num_clicks_t1 + num_clicks_t2  # Sum of clicks
  ) %>%
  ungroup() %>%
  select(contact_email, department, condition, link_key, Link,
         binary_click_t1, num_clicks_t1, 
         binary_click_t2, num_clicks_t2, 
         binary_click_all, num_clicks_all)

summary(lm(login ~ condition, data=result))


## Histograms for Click Data

# Function to calculate percentage and standard error remains the same
calc_stats <- function(x) {
  n <- length(x)
  p <- mean(x)
  se <- sqrt(p * (1 - p) / n)
  return(c(percent = p * 100, se = se * 100))
}

# Prepare data for plotting with updated labels
plot_data <- final_data %>%
  pivot_longer(cols = c(binary_click_t1, binary_click_t2, binary_click_all),
               names_to = "time_period",
               values_to = "clicked") %>%
  mutate(time_period = factor(time_period, 
                              levels = c("binary_click_t1", "binary_click_t2", "binary_click_all"),
                              labels = c("Email 1", "Email 2", "Overall"))) %>%
  mutate(condition = factor(condition, levels = c("control", "treatment"), labels = c("Control", "Treatment"))) %>%
  group_by(condition, time_period) %>%
  summarise(stats = list(calc_stats(clicked)), .groups = 'drop') %>%
  mutate(percent = map_dbl(stats, ~ .x["percent"]),
         se = map_dbl(stats, ~ .x["se"]))

# Create x variable as a factor with the desired order
plot_data <- plot_data %>%
  mutate(x_var = factor(paste(condition, time_period, sep = "_"),
                        levels = c("Control_Email 1", "Treatment_Email 1",
                                   "Control_Email 2", "Treatment_Email 2",
                                   "Control_Overall", "Treatment_Overall")))

# Create x-axis labels with updated font sizes and labels
x_labels <- c(
  "<span style='font-size:28pt'><b>Control</b></span><br><span style='font-size:20pt'>Email 1</span>",
  "<span style='font-size:28pt'><b>Treatment</b></span><br><span style='font-size:20pt'>Email 1</span>",
  "<span style='font-size:28pt'><b>Control</b></span><br><span style='font-size:20pt'>Email 2</span>",
  "<span style='font-size:28pt'><b>Treatment</b></span><br><span style='font-size:20pt'>Email 2</span>",
  "<span style='font-size:28pt'><b>Control</b></span><br><span style='font-size:20pt'>Overall</span>",
  "<span style='font-size:28pt'><b>Treatment</b></span><br><span style='font-size:20pt'>Overall</span>"
)

# Define custom color palette
custom_colors <- c(
  "Control" = "#1b9e77",
  "Treatment" = "#d95f02"
)

# Create the plot
p <- ggplot(plot_data, aes(x = x_var, y = percent, fill = condition)) +
  geom_bar(stat = "identity", width = 0.8) +
  # Place text lower inside the bars
  geom_text(aes(label = sprintf("%.1f%%", percent)),
            vjust = 3.5, color = "white", size = 12.5) +
  # Error bars
  geom_errorbar(aes(ymin = percent - se, ymax = percent + se),
                width = 0.2) +
  # Add dashed vertical line to separate Overall
  geom_vline(xintercept = 4.5, linetype = "dashed") +
  labs(title = "Binary Click Rates by Condition",
       x = NULL,
       y = "Percentage of Clicks") +
  scale_x_discrete(labels = x_labels) +
  scale_y_continuous(limits = c(0, 40), labels = function(x) paste0(x, "%"), expand = expansion(mult = c(0, 0.05))) +
  scale_fill_manual(values = custom_colors, name = NULL) +
  theme_minimal() +
  theme(
    legend.position = "none",
    axis.text.x = element_markdown(color = "black", size = 34),
    axis.text.y = element_text(color = "black", size = 34),
    axis.title.y = element_text(size = 34, margin = margin(r = 20)),
    axis.ticks.x = element_blank(),
    plot.margin = margin(t = 40, r = 20, b = 50, l = 20),
    panel.grid = element_blank(),
    plot.title = element_text(hjust = 0.5, size = 38, margin = margin(b = 20))
  )

# Save the updated plot
ggsave("combined_click_rates_updated.png", plot = p, width = 18, height = 12, dpi = 300)

## Analysis for Database Engagement

surveys <- tribble(
  ~name, ~id, ~discipline, ~condition,
  "chemistry-database", "SV_556wNdOiCPMcDkO", "chemistry", "treatment",
  "chemistry-department database", "SV_4JEt5BKaoDmtnXE", "chemistry", "control",
  "compsci-database", "SV_cO2cH592NPXb8t8", "compsci", "treatment",
  "compsci-department database", "SV_72LvDjIUQLpQlsW", "compsci", "control",
  "math-database", "SV_cO1KgPwFvS35UB8", "math", "treatment",
  "math-department database", "SV_8Jj8WIZJrhd5y8C", "math", "control",
  "ME-database", "SV_efjipNLwqTeo6zk", "ME", "treatment",
  "ME-department database", "SV_eXKiNxD0EZdiQRw", "ME", "control",
  "physics-database", "SV_cO6FTfuAZLMvZRQ", "physics", "treatment",
  "physics-department database", "SV_8jePppdXhNM9Ulo", "physics", "control"
)

fetch_and_process_survey <- function(survey_info) {
  survey_data <- qualtRics::fetch_survey(surveyID = survey_info$id, 
                                         verbose = FALSE, 
                                         label = FALSE, 
                                         convert = FALSE)
  
  survey_data %>%
    mutate(discipline = survey_info$discipline,
           condition = survey_info$condition)
}

all_surveys <- surveys %>%
  split(1:nrow(.)) %>%
  map_dfr(fetch_and_process_survey)

all_surveys$login <- 1


# Rename 'userEmail' to 'contact_email' in all_surveys
all_surveys <- all_surveys %>%
  rename(contact_email = userEmail) %>%
  select(contact_email, login) 

# First, let's count the number of logins for each email in all_surveys
login_counts <- all_surveys %>%
  group_by(contact_email) %>%
  summarise(logins = n())

# Now, let's join this with the original data and create our variables
result <- final_data %>%
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
  )

## Histograms for Database Engagement

# Function to calculate percentage and standard error remains the same
calc_stats <- function(x) {
  n <- length(x)
  p <- mean(x)
  se <- sqrt(p * (1 - p) / n)
  return(c(percent = p * 100, se = se * 100))
}

# Prepare data for the combined plot with updated labels
plot_data <- result %>%
  bind_rows(result %>% mutate(discipline = "Overall")) %>%
  mutate(discipline = factor(discipline, levels = c("Mathematics", "Physics", "Computer Science", "Chemistry", "Mechanical Engineering", "Overall"))) %>%
  mutate(condition = factor(condition, levels = c("control", "treatment"), labels = c("Control", "Treatment"))) %>%
  group_by(condition, discipline) %>%
  summarise(stats = list(calc_stats(login)), .groups = 'drop') %>%
  mutate(percent = map_dbl(stats, ~ .x["percent"]),
         se = map_dbl(stats, ~ .x["se"]))

# Create x variable as a factor with desired order
plot_data <- plot_data %>%
  mutate(x_var = factor(paste(condition, discipline, sep = "_"),
                        levels = c("Control_Mathematics", "Treatment_Mathematics",
                                   "Control_Physics", "Treatment_Physics",
                                   "Control_Computer Science", "Treatment_Computer Science",
                                   "Control_Chemistry", "Treatment_Chemistry",
                                   "Control_Mechanical Engineering", "Treatment_Mechanical Engineering",
                                   "Control_Overall", "Treatment_Overall")))

# Create x-axis labels with updated font sizes
x_labels <- c(
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>Math</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>Math</span>",
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>Phys</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>Phys</span>",
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>CS</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>CS</span>",
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>Chem</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>Chem</span>",
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>ME</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>ME</span>",
  "<span style='font-size:20pt'><b>Control</b></span><br><span style='font-size:16pt'>Overall</span>",
  "<span style='font-size:20pt'><b>Treatment</b></span><br><span style='font-size:16pt'>Overall</span>"
)

# Define custom color palette
custom_colors <- c(
  "Control" = "#1b9e77",
  "Treatment" = "#d95f02"
)

# Create the plot
p2 <- ggplot(plot_data, aes(x = x_var, y = percent, fill = condition)) +
  geom_bar(stat = "identity", width = 0.8) +
  # Place text lower inside the bars
  geom_text(aes(label = sprintf("%.1f%%", percent)), 
            vjust = 2.5, color = "white", size = 8) +
  # Error bars
  geom_errorbar(aes(ymin = percent - se, ymax = percent + se), 
                width = 0.2) +
  # Adjust the position of the asterisk
  geom_text(data = plot_data %>% filter(condition == "Treatment" & discipline == "Overall"),
            aes(x = x_var, y = percent + se + 2, label = "*"), 
            vjust = 0, color = "black", size = 14) +
  # Add dashed vertical line to separate Overall
  geom_vline(xintercept = 10.5, linetype = "dashed") +
  labs(title = "Database Login Rates by Condition",
       x = NULL,
       y = "Percentage of Logins") +
  scale_x_discrete(labels = x_labels) +
  scale_y_continuous(limits = c(0, 30), labels = function(x) paste0(x, "%"), expand = expansion(mult = c(0, 0.05))) +
  scale_fill_manual(values = custom_colors, name = NULL) +
  theme_minimal() +
  theme(
    legend.position = "none",
    axis.text.x = element_markdown(color = "black", size = 20),
    axis.text.y = element_text(color = "black", size = 20),
    axis.title.y = element_text(size = 24, margin = margin(r = 20)),
    axis.ticks.x = element_blank(),
    plot.margin = margin(t = 40, r = 20, b = 50, l = 20),
    panel.grid = element_blank(),
    plot.title = element_text(hjust = 0.5, size = 28, margin = margin(b = 20))
  )

# Save the updated plot
ggsave("combined_login_rates_updated.png", plot = p2, width = 18, height = 10, dpi = 300)


# Function to calculate percentage and standard error
calc_stats <- function(x) {
  n <- length(x)
  p <- mean(x)
  se <- sqrt(p * (1 - p) / n)
  return(c(percent = p * 100, se = se * 100))
}

# Function to calculate y_offset
calculate_y_offset <- function(discipline, condition) {
  if (discipline == "Overall") {
    return(ifelse(condition == "Control", -0.2, 0.2))
  } else {
    return(0)
  }
}

# Prepare data for the forest plot
plot_data <- result %>%
  bind_rows(result %>% mutate(discipline = "Overall")) %>%
  mutate(
    discipline = factor(discipline, levels = rev(c("Mechanical Engineering", "Chemistry", "Computer Science", "Physics", "Mathematics", "Overall"))),
    condition = factor(condition, levels = c("control", "treatment"), labels = c("Control", "Treatment"))
  ) %>%
  group_by(condition, discipline) %>%
  summarise(stats = list(calc_stats(login)), .groups = 'drop') %>%
  mutate(
    percent = map_dbl(stats, ~ .x["percent"]),
    se = map_dbl(stats, ~ .x["se"]),
    ci_lower = percent - 1.96 * se,
    ci_upper = percent + 1.96 * se,
    y_offset = mapply(calculate_y_offset, discipline, condition)  # Add this line
  )

# Create the forest plot
p_forest <- ggplot(plot_data, aes(x = percent, y = discipline, color = condition)) +
  # Add error bars for confidence intervals
  geom_errorbarh(aes(xmin = ci_lower, xmax = ci_upper), height = 0.3, position = position_dodge(width = 0.7), linewidth = 0.8) +
  # Add points for the percentage estimates
  geom_point(position = position_dodge(width = 0.7), size = 3) +
  # Add vertical line at 0%
  geom_vline(xintercept = 0, linetype = "solid", color = "gray", linewidth = 0.5) +
  # Highlight the Overall data in red
  geom_errorbarh(
    data = plot_data %>% filter(discipline == "Overall"),
    aes(xmin = ci_lower, xmax = ci_upper, y = as.numeric(discipline) + y_offset),
    height = 0.2,
    position = position_dodge(width = 0),
    linewidth = 1
  ) +
  # Highlight the Overall data points
  geom_point(
    data = plot_data %>% filter(discipline == "Overall"),
    aes(y = as.numeric(discipline) + y_offset),
    position = position_dodge(width = 0),
    size = 7
  ) +
  # Add text annotations for Overall percentages
  geom_text(
    data = plot_data %>% filter(discipline == "Overall"),
    aes(
      y = as.numeric(discipline) + y_offset,
      label = sprintf("%.1f", percent)
    ),
    position = position_dodge(width = 0),
    size = 2.5,
    color = "white",
    fontface = "bold"
  ) +
  # Add horizontal dashed line between Mechanical Engineering and Overall
  geom_hline(
    yintercept = which(levels(plot_data$discipline) == "Overall") + 0.5,
    linetype = "dashed", color = "black", linewidth = 0.5
  ) +
  # Add horizontal solid line between Mechanical Engineering and Overall
  geom_hline(
    yintercept = which(levels(plot_data$discipline) == "Overall") - 0.5,
    linetype = "solid", color = "black", linewidth = 0.75
  ) +
  # Add asterisk between Overall points to indicate significance
  geom_text(
    data = data.frame(x = 19, y = which(levels(plot_data$discipline) == "Overall"), label = "*"),
    aes(x = x, y = y, label = label),
    color = "black",
    size = 15,
    vjust = 0.5
  ) +
  labs(title = "Database Login Rates by Discipline and Condition",
       x = "Percentage of Logins",
       y = NULL,
       color = "Condition") +
  scale_x_continuous(labels = function(x) paste0(x, "%"), limits = c(0, NA)) +
  scale_color_manual(values = c("Control" = "#1b9e77", "Treatment" = "#d95f02")) +
  # Adjust the theme
  theme_minimal() +
  theme(
    legend.position = "top",
    legend.title = element_text(size = 18),
    legend.text = element_text(size = 16),
    axis.text.y = element_text(size = 18),
    axis.text.x = element_text(size = 16),
    axis.title.x = element_text(size = 20, margin = margin(t = 10)),
    plot.title = element_text(hjust = 0.5, size = 24, margin = margin(b = 20)),
    plot.margin = margin(t = 20, r = 30, b = 20, l = 20),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),  # Remove vertical grid lines
    panel.grid.major.y = element_blank()
  )

# Save the forest plot
ggsave("database_login_rates_forest_updated.png", plot = p_forest, width = 12, height = 8, dpi = 300)
