library(dplyr)
library(readr)

# Read in the CSV data
data <- read_csv("email-list.csv")

# Combine 'university' and 'discipline' to form 'department'
data <- data %>%
  mutate(department = paste(university, discipline, sep = "-"))

# Count the number of seminars per department
seminar_counts <- data %>%
  group_by(department) %>%
  summarize(seminar_count = n()) %>%
  arrange(seminar_count)

# Define bins based on the seminar counts by department
bins <- cut(seminar_counts$seminar_count, 
            breaks = c(0, 1, 3, 5,7,11,17, 28),
            include.lowest = TRUE,
            right = TRUE)

# Add bin information to the seminar counts
seminar_counts <- seminar_counts %>%
  mutate(bin_category = bins)

# Summarize and print bins
bin_summary <- seminar_counts %>%
  group_by(bin_category) %>%
  summarize(department_count = n(),
            total_seminars = sum(seminar_count))

# Print the summary
print(bin_summary)

# For visualising distribution before randomization
seminar_counts %>%
  select(seminar_count) %>%
  table() %>%
  print()

# Function to perform stratified randomization
stratified_randomize <- function(data, strata_col, group_col, num_groups) {
  data %>%
    group_by(across(all_of(strata_col))) %>%
    mutate(
      {{group_col}} := sample(rep(1:num_groups, each = ceiling(n() / num_groups), length.out = n()))
    ) %>%
    ungroup()
}

# Define number of groups
num_groups <- 2

# Apply stratified randomization
randomized_data <- stratified_randomize(seminar_counts, "bin_category", "group", num_groups)

# Check the resulting distribution
randomized_distribution <- randomized_data %>%
  group_by(bin_category, group) %>%
  summarize(department_count = n(), total_seminars = sum(seminar_count), .groups = 'drop')

print(randomized_distribution)

# View the first few rows of the randomized data
head(randomized_data)
