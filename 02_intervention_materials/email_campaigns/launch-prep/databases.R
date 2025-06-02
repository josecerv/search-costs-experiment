library(qualtRics)
library(dplyr)
library(purrr)



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