library(jsonlite)

# Read the JSON data from the file
json_data <- fromJSON("universities.json")

# Convert the parsed data into a dataframe
df <- as.data.frame(json_data)

# Save the dataframe as a CSV file
write.csv(df, "university_departments.csv", row.names = FALSE)
