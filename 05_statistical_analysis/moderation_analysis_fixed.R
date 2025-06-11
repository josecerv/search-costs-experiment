# Fixed Moderation Analysis Functions
# This file contains functions for running moderation analyses that match the main effects table format

# Function to run moderation analysis for a single demographic group
run_moderation_by_demographic <- function(demographic, moderator_var, moderator_label, 
                                        base_controls, extended_controls, 
                                        exclude_controls = NULL, center = TRUE) {
  
  # Get functions and data from parent environment
  data <- get("data", envir = parent.frame())
  run_regression <- get("run_regression", envir = parent.frame())
  create_regression_table <- get("create_regression_table", envir = parent.frame())
  
  # Check if moderator variable exists
  if (!moderator_var %in% names(data)) {
    cat(sprintf("\\textbf{Error}: Moderator variable '%s' not found in dataset.\\\\\\\\", moderator_var))
    return(invisible(NULL))
  }
  
  # Center the moderator if requested
  if (center) {
    data[[paste0(moderator_var, "_centered")]] <- scale(data[[moderator_var]], scale = FALSE)[,1]
    mod_var_name <- paste0(moderator_var, "_centered")
  } else {
    mod_var_name <- moderator_var
  }
  
  # Define outcome variables for this demographic
  pct_var <- paste0("pct_", demographic)
  count_var <- paste0("num_", demographic)
  any_var <- paste0("has_any_", demographic)
  
  # Remove excluded controls
  base_controls_to_use <- base_controls
  extended_controls_to_use <- extended_controls
  if (!is.null(exclude_controls)) {
    base_controls_to_use <- setdiff(base_controls_to_use, exclude_controls)
    extended_controls_to_use <- setdiff(extended_controls_to_use, exclude_controls)
  }
  
  # Run 6 models: 3 outcomes × 2 model types
  models <- list()
  
  # Model 1: % demographic with simple controls
  formula1 <- paste0(pct_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(base_controls_to_use, collapse = " + "))
  model1 <- run_regression(formula1, data)
  
  # Model 2: % demographic with extended controls
  formula2 <- paste0(pct_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(c(base_controls_to_use, extended_controls_to_use), collapse = " + "))
  model2 <- run_regression(formula2, data)
  
  # Model 3: Count demographic with simple controls
  formula3 <- paste0(count_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(base_controls_to_use, collapse = " + "))
  model3 <- run_regression(formula3, data)
  
  # Model 4: Count demographic with extended controls
  formula4 <- paste0(count_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(c(base_controls_to_use, extended_controls_to_use), collapse = " + "))
  model4 <- run_regression(formula4, data)
  
  # Model 5: Any demographic with simple controls
  formula5 <- paste0(any_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(base_controls_to_use, collapse = " + "))
  model5 <- run_regression(formula5, data)
  
  # Model 6: Any demographic with extended controls
  formula6 <- paste0(any_var, " ~ treatment * ", mod_var_name, " + ", 
                     paste(c(base_controls_to_use, extended_controls_to_use), collapse = " + "))
  model6 <- run_regression(formula6, data)
  
  models <- list(model1, model2, model3, model4, model5, model6)
  
  # Create proper demographic label
  demographic_label <- switch(demographic,
                            "urm" = "URM",
                            "black" = "Black", 
                            "hispanic" = "Hispanic",
                            demographic)
  
  # Create table using the same function as main effects
  title <- paste0("Effect on ", demographic_label, " Speakers: Moderation by ", moderator_label)
  label <- paste0("tab:mod_", demographic, "_", gsub("[^a-zA-Z0-9]", "_", tolower(moderator_var)))
  
  create_regression_table(models, title, label, 
                         demographic_group = demographic_label,
                         is_moderator = TRUE, 
                         moderator_name = moderator_label)
  
  # Build list of model info to return
  moderation_models <- list()
  
  # Find interaction term name
  interaction_name <- paste0("treatment:", mod_var_name)
  if (!is.null(model1) && !interaction_name %in% names(coef(model1))) {
    interaction_name <- paste0(mod_var_name, ":treatment")
  }
  
  # Add all models with proper metadata
  outcome_labels <- c(paste0("% ", demographic_label), paste0("% ", demographic_label),
                     paste0("Count ", demographic_label), paste0("Count ", demographic_label),
                     paste0("Any ", demographic_label), paste0("Any ", demographic_label))
  model_types <- rep(c("Simple", "Extended"), 3)
  
  for (i in seq_along(models)) {
    if (!is.null(models[[i]])) {
      moderation_models <- append(moderation_models, list(
        list(model = models[[i]], 
             analysis = paste("Moderation by", moderator_label),
             outcome = outcome_labels[i],
             model_type = model_types[i],
             var_names = c("treatment", mod_var_name, interaction_name),
             var_labels = c("Treatment", moderator_label, paste("Treatment ×", moderator_label)))
      ))
    }
  }
  
  # Return the model info list instead of trying to assign
  return(list(models = models, model_info_list = moderation_models))
}

# Main function to run all moderation analyses for a given moderator
run_comprehensive_moderation_fixed <- function(moderator_var, moderator_label, 
                                             exclude_controls = NULL, center = TRUE) {
  
  # Get required objects from parent environment
  data <- get("data", envir = parent.frame())
  base_controls <- get("base_controls", envir = parent.frame())
  extended_controls <- get("extended_controls", envir = parent.frame())
  
  # Collect all model info
  all_model_info <- list()
  
  # Run moderation for each demographic group
  demographics <- c("urm", "black", "hispanic")
  
  for (demo in demographics) {
    cat("\\subsection{", toupper(demo), " Speakers}\n\n")
    result <- run_moderation_by_demographic(demo, moderator_var, moderator_label,
                                          base_controls, extended_controls,
                                          exclude_controls, center)
    # Collect the model info
    if (!is.null(result$model_info_list)) {
      all_model_info <- append(all_model_info, result$model_info_list)
    }
    cat("\n")
  }
  
  # Return the model info list
  return(invisible(all_model_info))
}

# Function to extract only significant interactions for summary
extract_significant_interactions <- function(all_models_list) {
  sig_interactions <- data.frame(
    Analysis = character(),
    Outcome = character(),
    Model = character(),
    Coefficient = numeric(),
    SE = numeric(),
    t_stat = numeric(),
    p_value = numeric(),
    Significance = character(),
    stringsAsFactors = FALSE
  )
  
  for (model_info in all_models_list) {
    if (!is.null(model_info$model) && 
        !is.null(model_info$var_names) && 
        length(model_info$var_names) >= 3) {
      
      # Only look at interaction models
      if (grepl("Moderation", model_info$analysis)) {
        model <- model_info$model
        interaction_name <- model_info$var_names[3]
        
        if (interaction_name %in% names(coef(model))) {
          coef_val <- coef(model)[interaction_name]
          se_val <- model$cluster_se[interaction_name]
          t_val <- coef_val / se_val
          p_val <- 2 * pt(-abs(t_val), df = length(model$residuals) - length(coef(model)))
          
          # Only include if interaction is significant at p < 0.1
          if (p_val < 0.1) {
            sig <- ifelse(p_val < 0.001, "***",
                         ifelse(p_val < 0.01, "**",
                               ifelse(p_val < 0.05, "*", "+")))
            
            sig_interactions <- rbind(sig_interactions, data.frame(
              Analysis = model_info$analysis,
              Outcome = model_info$outcome,
              Model = model_info$model_type,
              Coefficient = coef_val,
              SE = se_val,
              t_stat = t_val,
              p_value = p_val,
              Significance = sig,
              stringsAsFactors = FALSE
            ))
          }
        }
      }
    }
  }
  
  return(sig_interactions)
}