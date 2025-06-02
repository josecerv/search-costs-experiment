# Load necessary libraries
library(dplyr)
library(stringr)
library(tidyr)
library(uuid) # Load library for UUID generation

# Setting the seed for reproducibility
set.seed(42)

# Helper functions
concat_seminar_names <- function(names) {
  paste(names, collapse = ", ")
}

extract_first_email <- function(emails) {
  email_list <- str_split(emails, pattern = "[,;\\s]+")[[1]]
  return(trimws(email_list[1]))
}

has_multiple_emails <- function(emails) {
  email_list <- str_split(emails, pattern = "[,;\\s]+")[[1]]
  return(length(email_list) > 1)
}

extract_first_full_contact_name <- function(names) {
  name_list <- str_split(names, pattern = "[,;&]+")[[1]]
  return(trimws(name_list[1]))
}

particles <- c("de", "van", "von", "der", "di", "la", "le")

create_professor_salutation <- function(name) {
  if (is.na(name)) return(NA)  # Handle NA values
  
  if (str_detect(name, "William T\\. Pennington Jr\\.")) {
    return("Professor Pennington Jr.")
  }
  if (str_detect(name, "Dorina Mitrea, Ph\\.D\\.")) {
    return("Professor Mitrea")
  }
  if (str_detect(name, "John L\\. Wood, Ph\\.D\\.")) {
    return("Professor Wood")
  }
  if (str_detect(name, "Sean Andersson, Ph\\.D\\.")) {
    return("Professor Andersson")
  }
  if (str_detect(name, "Steve Shepard Jr\\.")) {
    return("Professor Shepard Jr.")
  }
  
  name <- str_remove_all(name, "(?i)\\b(Ph\\.D\\.|PhD|Dr\\.|Prof\\.|Dean|Jr\\.?|III|II|IV|V|VI)\\b")
  name <- str_squish(str_remove_all(name, "[.,]$"))
  name_split <- str_split(name, pattern = "\\s+")[[1]]
  
  if (length(name_split) >= 2 && tolower(name_split[length(name_split) - 1]) %in% particles) {
    last_name <- paste(name_split[length(name_split) - 1], name_split[length(name_split)])
  } else {
    last_name <- name_split[length(name_split)]
  }
  
  last_name <- str_remove_all(last_name, "[.,]$")
  salutation <- paste("Professor", str_trim(last_name))
  return(salutation)
}

# Function to clean and transform seminar names based on specific conditions
clean_seminar_name <- function(seminar_name) {
  # Keywords with singular and plural forms
  keywords <- c("Seminar", "Seminars", "Colloquium", "Colloquia", "Talk", "Talks")
  
  # Identify if seminar_name is a single word
  word_count <- str_count(seminar_name, "\\w+")
  
  if (word_count == 1) {
    if (tolower(seminar_name) %in% tolower(keywords)) {
      return(tolower(seminar_name))
    } else {
      return(paste(seminar_name, "Seminar"))
    }
  } else {
    return(seminar_name)
  }
}

# Ensure this function handles multiple seminar names correctly
create_body_message <- function(contact_type, seminar_names) {
  cleaned_seminar_names <- sapply(str_split(seminar_names, ",\\s*")[[1]], clean_seminar_name)
  cleaned_seminar_names <- paste(cleaned_seminar_names, collapse = ", ")
  
  body <- if_else(
    contact_type == "department_chair",
    "the current chair of your department",
    paste("the organizer of your department’s", cleaned_seminar_names)
  )
  
  return(body)
}

create_database_message <- function(condition) {
  if (condition == "control") {
    return("departments in your field that you can search to enhance the diversity of your academic seminar series, and you can find it here")
  } else if (condition == "treatment") {
    return("scholars in your field who might enhance the diversity of your academic seminar series, and you can find it here")
  } else {
    return("")
  }
}

# Read in the main data
data <- read.csv('email-list.csv', header = TRUE, encoding = "UTF-8") %>%
  select(university, discipline, seminar_name, contact_name, contact_email, department_chair_name, department_chair_email, contact_type)

# Read in the key data for link generation
key_data <- read.csv('randomized data - links.csv', header = TRUE) %>%
  select(condition, department, link, campaign) # Ensure correct columns are selected

# Read in the randomized data for condition assignment
randomized_data <- read.csv('randomized_data.csv', header = TRUE) %>%
  select(department, condition)

# Create a mapping of condition and department to prefix
prefix_map <- key_data %>%
  unite("condition_department", condition, department, sep = "_") %>%
  distinct(condition_department, campaign, link) # Ensure link is included

# Merge in the randomized data to assign the correct condition
data <- data %>%
  mutate(department = paste(university, discipline, sep = "-")) %>%
  left_join(randomized_data, by = "department")

# Debugging: Check distribution after assignment
print(table(data$condition))

# Now we can safely merge the condition and discipline to create condition_department
data <- data %>%
  unite("condition_department", condition, discipline, sep = "_", remove = FALSE)

# Group by contact_email and collapse seminar_names
collapsed_contact <- data %>%
  group_by(contact_name, contact_email) %>%
  summarise(
    university = first(university),
    discipline = first(discipline),
    department = first(department),
    condition = first(condition),
    condition_department = first(condition_department),
    seminar_names = concat_seminar_names(seminar_name),
    contact_type = first(contact_type), # Preserve contact_type
    .groups = 'drop'
  ) %>%
  mutate(
    flag_multiple_emails = sapply(contact_email, has_multiple_emails),
    contact_email = sapply(contact_email, extract_first_email),
    original_name = contact_name,
    contact_name = case_when(
      contact_type == "faculty" ~ sapply(contact_name, function(name) create_professor_salutation(name)),
      TRUE ~ sapply(contact_name, function(name) extract_first_full_contact_name(name))
    ),
    contact_type = case_when(
      contact_type == "faculty" ~ "faculty",
      TRUE ~ "seminar_contact"
    ),
    salutation = case_when(
      contact_type == "faculty" | contact_type == "department_chair" ~ sapply(contact_name, function(name) create_professor_salutation(name)),
      TRUE ~ "Seminar Organizer"
    ),
    body = sapply(seminar_names, function(x) create_body_message("seminar_contact", x)), # Use sapply to iterate over each seminar_names
    database = sapply(condition, create_database_message)
  ) %>%
  ungroup()

# Ensure seq_id has the same number of unique ids as the number of rows in collapsed_contact
unique_seq_ids <- sample(1:nrow(collapsed_contact) * 10, nrow(collapsed_contact), replace = FALSE)
unique_uuids <- replicate(nrow(collapsed_contact), UUIDgenerate())

collapsed_contact <- collapsed_contact %>%
  mutate(seq_id = unique_seq_ids) %>%
  mutate(link_key = paste0(unique_uuids)) %>%
  left_join(prefix_map, by = "condition_department") %>%
  mutate(link_key = paste0(campaign, "-", link_key)) %>%
  select(contact_name, contact_email, department, seminar_names, contact_type, salutation, original_name, body, link_key, condition, link, database)

# Count the number of unique department_chair_name per department
chair_counts <- data %>%
  group_by(university, discipline) %>%
  summarise(department_chair_count = n_distinct(department_chair_name), .groups = 'drop')

# Merge the chair_counts back to the original data to flag duplicates
data_with_flags <- data %>%
  left_join(chair_counts, by = c("university", "discipline")) %>%
  mutate(flag_multiple_chairs = if_else(department_chair_count > 1, TRUE, FALSE))

# Use the data_with_flags to generate collapsed_chair
collapsed_chair <- data_with_flags %>%
  group_by(department_chair_name, department_chair_email) %>%
  summarise(
    university = first(university),
    discipline = first(discipline),
    department = first(department),
    condition = first(condition),
    condition_department = first(condition_department),
    seminar_names = concat_seminar_names(seminar_name),
    flag_multiple_chairs = first(flag_multiple_chairs),
    contact_type = "department_chair",
    .groups = 'drop'
  ) %>%
  ungroup()

# Ensure seq_id has the same number of unique ids as the number of rows in collapsed_chair
unique_seq_ids_chair <- sample(1:nrow(collapsed_chair) * 10, nrow(collapsed_chair), replace = FALSE)
unique_uuids_chair <- replicate(nrow(collapsed_chair), UUIDgenerate())

collapsed_chair <- collapsed_chair %>%
  mutate(seq_id = unique_seq_ids_chair) %>%
  mutate(link_key = paste0(unique_uuids_chair)) %>%
  left_join(prefix_map, by = "condition_department") %>%
  mutate(link_key = paste0(campaign, "-", link_key)) %>%
  mutate(
    original_name = department_chair_name,
    contact_name = department_chair_name,
    contact_email = department_chair_email,
    salutation = sapply(department_chair_name, function(name) create_professor_salutation(name)),
    body = "the current chair of your department",
    database = sapply(condition, create_database_message)
  ) %>%
  select(contact_name, contact_email, department, seminar_names, contact_type, salutation, original_name, body, link_key, condition, link, database)

# Combine collapsed_contact and collapsed_chair
combined_data <- bind_rows(collapsed_contact, collapsed_chair)

# Remove rows with NA in contact_email
final_data <- combined_data %>%
  filter(!is.na(contact_email))

# Print the distribution of the condition to verify correct assignment
print(table(final_data$condition))

# Print final results to check
print(final_data)

# Identify duplicates based on contact_email and link_key
duplicate_contacts <- final_data %>%
  group_by(contact_email) %>%
  filter(n() > 1) %>%
  ungroup()

duplicate_link_keys <- final_data %>%
  group_by(link_key) %>%
  filter(n() > 1) %>%
  ungroup()

# Create a summary table for the duplicates
duplicate_summary <- duplicate_contacts %>%
  group_by(contact_email) %>%
  summarise(
    count = n(),
    contact_names = paste(contact_name, collapse = "; "),
    departments = paste(department, collapse = "; "),
    seminar_names = paste(seminar_names, collapse = "; "),
    conditions = paste(condition, collapse = "; ")
  ) %>%
  arrange(desc(count))

duplicate_link_key_summary <- duplicate_link_keys %>%
  group_by(link_key) %>%
  summarise(
    count = n(),
    contact_emails = paste(contact_email, collapse = "; "),
    contact_names = paste(contact_name, collapse = "; ")
  ) %>%
  arrange(desc(count))

# Print the duplicates summary table
print(duplicate_summary)
print(duplicate_link_key_summary)

# Optionally: View the duplicates summary table in a viewer
View(duplicate_summary)
View(duplicate_link_key_summary)

# View additional debug info if needed
View(final_data)

# Write the final cleaned data to a CSV file
final_data[] <- lapply(final_data, function(x) if(is.character(x)) enc2utf8(x) else x)
write.csv(final_data, "email-launch.csv", row.names = FALSE, fileEncoding = "UTF-8")
