library(lmerTest)
library(lme4)
library(Matrix)
library(parallel)

# Define parameters
m <- 730  # Number of departments
n <- 3  # Number of seminars per department
baseline_invitation_rate <- 5  # Baseline mean number of invitations
treatment_effect <- 0.5  # Expected increase in invitations due to treatment

# Standard deviations
sigma_u <- 1.5  # Between-department SD
sigma_e <- 2.5  # Within-department (seminar) SD

# Generate treatment assignment (half treatment, half control)
treatment <- rep(c(0, 1), each = m/2)

# Function to run one simulation
run_simulation <- function(i) {
  sim_data <- data.frame(
    department = rep(1:m, each = n),
    treatment = rep(treatment, each = n)
  )
  sim_data$u_d <- rep(rnorm(m, 0, sigma_u), each = n)
  sim_data$epsilon_s <- rnorm(m * n, 0, sigma_e)
  # Generate invitations based on mixed-effects model assumptions
  sim_data$invitations <- baseline_invitation_rate + treatment_effect * sim_data$treatment + sim_data$u_d + sim_data$epsilon_s
  
  # Fit mixed-effects model
  fit <- lmer(invitations ~ treatment + (1 | department), data = sim_data)
  return(coef(summary(fit))["treatment", "Pr(>|t|)"])  # Extract p-value for treatment
}

# Number of simulations for power analysis
n_sim <- 1000

# Run simulations in parallel
cl <- makeCluster(detectCores() - 1)  # Use all but one core
clusterExport(cl, list("m", "n", "baseline_invitation_rate", "treatment_effect", "sigma_u", "sigma_e", "treatment", "run_simulation", "lmer", "coef", "summary"))

p_values <- parSapply(cl, 1:n_sim, run_simulation)
stopCluster(cl)

# Calculate power
power <- mean(p_values < 0.05)
print(power)


### Clustered standard errors
library(lmerTest)
library(lme4)
library(Matrix)
library(parallel)
library(clubSandwich)
library(lmtest)
library(sandwich)

# Define parameters
m <- 730  # Number of departments
n <- 3  # Number of seminars per department
baseline_invitation_rate <- 5  # Baseline mean number of invitations
treatment_effect <- 0.5  # Expected increase in invitations

# Standard deviations
sigma_u <- 1.5  # Between-department SD
sigma_e <- 2.5  # Within-department (seminar) SD

# Generate treatment assignment (half treatment, half control)
treatment <- rep(c(0, 1), each = m/2)

# Function to run one simulation
run_simulation_clustered_OLS <- function(i) {
  sim_data <- data.frame(
    department = rep(1:m, each = n),
    treatment = rep(treatment, each = n)
  )
  sim_data$u_d <- rep(rnorm(m, 0, sigma_u), each = n)
  sim_data$epsilon_s <- rnorm(m * n, 0, sigma_e)
  sim_data$invitations <- baseline_invitation_rate + treatment_effect * sim_data$treatment + sim_data$u_d + sim_data$epsilon_s
  
  fit <- lm(invitations ~ treatment, data = sim_data)
  cluster_se <- vcovCL(fit, cluster = sim_data$department)
  wald_test <- coeftest(fit, vcov = cluster_se)
  
  return(wald_test["treatment", "Pr(>|t|)"])  # Extract p-value for treatment
}

# Number of simulations for power analysis
n_sim <- 1000

# Run simulations in parallel for OLS with Clustered SE
cl <- makeCluster(detectCores() - 1)  # Use all but one core
clusterExport(cl, list("m", "n", "baseline_invitation_rate", "treatment_effect", "sigma_u", "sigma_e", "treatment", "run_simulation_clustered_OLS", "lm", "vcovCL", "coeftest"))
clusterEvalQ(cl, {
  library(clubSandwich)
  library(lmtest)
  library(sandwich)
})

p_values_clustered_OLS <- parSapply(cl, 1:n_sim, run_simulation_clustered_OLS)
stopCluster(cl)

# Calculate power
power <- mean(p_values_clustered_OLS < 0.05)
print(power)


