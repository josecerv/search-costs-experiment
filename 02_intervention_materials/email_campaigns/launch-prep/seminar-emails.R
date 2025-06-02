# Load required libraries
library(tidyverse)
library(readxl)

# Path to the Excel file
file_path <- "master-spreadsheet.xlsx"

# Define the sheet names or use readxl to get them
sheets <- excel_sheets(file_path)

# Regex pattern for a basic email validation
email_pattern <- "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

# Function to extract and validate emails
extract_valid_emails <- function(text) {
  if (is.na(text) || text == "" || text == "N/A") return(NA_character_)
  
  # Split text by potential delimiters and trim whitespace
  emails <- unlist(str_split(text, "[,;\\s]+")) %>%
    str_trim()
  
  # Extract valid emails using regex
  valid_emails <- str_subset(emails, email_pattern)
  
  # Return emails or NA if no valid emails are found
  return(ifelse(length(valid_emails) > 0, paste(valid_emails, collapse = "; "), NA_character_))
}

# Create an empty dataframe to store combined data
combined_data <- tibble()

# Loop through each sheet, read the data and extract necessary columns
for (sheet in sheets) {
  sheet_data <- read_excel(file_path, sheet = sheet)
  
  # Select important columns, add the discipline column with the sheet name, and clean contact emails
  selected_data <- sheet_data %>%
    mutate(discipline = sheet,
           contact_email = map_chr(`Contact Email Address`, extract_valid_emails)) %>%
    select(university = `School`,
           discipline,
           seminar_name = `Name of Seminar/Colloquia`,
           contact_name = `Name of Contact`,
           contact_email,
           department_chair_name = `Department Chair Name`,
           department_chair_email = `Department Chair Email`,
           notes_for_0_speakers = `Notes for 0 speakers in Fall 2023`) %>%
    # Replace NA values in notes_for_0_speakers with "Available"
    replace_na(list(notes_for_0_speakers = "Available"))
  
  # Append to combined_data
  combined_data <- bind_rows(combined_data, selected_data)
}

# View the combined dataframe
print(combined_data)



## Final sample size

final_sample <- combined_data |> 
  filter(!is.na(contact_email) | !is.na(department_chair_email)) |> 
  filter(notes_for_0_speakers != "Not available at all")

final_sample |> 
  count(discipline)

final_sample_w_seminar <- final_sample |> 
  filter(!is.na(contact_email))

### FINAL SAMPLE WITH DEPT CHAIR + SEMINAR

# Combine all email columns into a single vector
email_columns <- c("contact_email", "department_chair_email")  # Add all email-related columns
all_emails <- unlist(final_sample[email_columns])

# Count the number of unique email addresses
unique_emails <- unique(all_emails)
num_unique_emails <- length(unique_emails)

# Print the result
cat("Number of unique email addresses:", num_unique_emails, "\n")

### FINAL SAMPLE WITH SEMINAR ONLY

# Combine all email columns into a single vector
email_columns <- c("contact_email")  # Add all email-related columns
all_emails <- unlist(final_sample_w_seminar[email_columns])

# Count the number of unique email addresses
unique_emails <- unique(all_emails)
num_unique_emails <- length(unique_emails)

# Print the result
cat("Number of unique email addresses:", num_unique_emails, "\n")


## seminars by department

department_seminar_counts <- final_sample %>%
  group_by(university, discipline) %>%
  summarise(num_seminars = n()) %>%
  arrange(university, discipline)

department_seminar_counts %>%
  ungroup() |> 
  summarise(avg_seminars = mean(num_seminars))


##write.csv(final_sample, "final_sample.csv", row.names = FALSE)
