# Load necessary library
library(readr)

# Read the main CSV file
data <- read.csv("email-launch-two.csv")

# Define path to 'send-two' folder
output_folder <- "send-two"

# Number of observations in each split
n <- 150

# Calculate the sequence of data frames
split_data <- split(data, (seq(nrow(data)) - 1) %/% n)

# Create the row to be appended
new_row <- data.frame(
  "Professor Milkman", "kmilkman@wharton.upenn.edu", "University of Michigan-Computer Science",
  "Systems Seminars", "faculty", "Professor Milkman", "Kang G. Shin",
  "the organizer of your department's Systems Seminars",
  "ST-7f9ee741-7169-4f92-af93-b592e06b0641", "treatment", "https://whr.tn/4cukZn7",
  "scholars in your field who might enhance the diversity of your academic seminar series, and you can find it",
  1, 0, 0, 0
)

# Assign meaningful column names to the row
colnames(new_row) <- colnames(data)

# Loop through each split and write to CSV
for (i in seq_along(split_data)) {
  # Combine the split data with the new row
  split_data_with_row <- rbind(split_data[[i]], new_row)
  
  # Define the filename
  file_name <- file.path(output_folder, paste0("email-launch-part-", i, ".csv"))
  
  # Write the data to CSV
  write.csv(split_data_with_row, file_name, row.names = FALSE)
}
