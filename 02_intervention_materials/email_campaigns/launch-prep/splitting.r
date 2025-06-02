# Load the required library
library(dplyr)

# Read the CSV files
email_launch <- read.csv("email-launch.csv")
email_launch_two <- read.csv("email-launch-two.csv")

# Find individuals in email_launch but not in email_launch_two
not_in_second_launch <- anti_join(email_launch, email_launch_two, by = "contact_email")

# Save the result to a dataframe
result_df <- not_in_second_launch