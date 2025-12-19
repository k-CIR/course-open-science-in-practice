
# Simulate lifestyle + mental health dataset
n <- 120

set.seed(2025)

# Sex: 1 = male, 2 = female, 3 = other
# Mostly binary with a few "other"
sex <- sample(
  x = c(1, 2, 3),
  size = n,
  replace = TRUE,
  prob = c(0.48, 0.48, 0.04)
)

# Age: normal around 40, truncated to 16–80
age <- round(rnorm(n, mean = 40, sd = 15))
age <- pmin(pmax(age, 16), 80)

# How did you hear about the survey?
survey <- sample(
  x = 1:4,
  size = n,
  replace = TRUE,
  prob = c(0.05, 0.60, 0.15, 0.20)
)

# ----------------------------
# Position
# 1 = student
# Everyone ≤25 is position 1
# + exactly 10 observations aged 26–40 also position 1
# Remaining positions distributed: 2 ~30%, 3 ~50%, 4 ~15%, 5 = rest
# ----------------------------

position <- rep(NA, n)

# All age ≤25 are students
position[age <= 25] <- 1

# Add 10 students among ages 26–40
eligible <- which(age >= 26 & age <= 40 & is.na(position))
extra_students <- sample(eligible, size = min(10, length(eligible)))
position[extra_students] <- 1

# Remaining observations
remaining <- which(is.na(position))
n_remain <- length(remaining)

position[remaining] <- sample(
  x = c(2, 3, 4, 5),
  size = n_remain,
  replace = TRUE,
  prob = c(0.30, 0.50, 0.15, 0.05)
)

# ----------------------------
# TimeHere (years at institution)
# Ranges depend on age, with lower values more common
# ----------------------------

TimeHere <- numeric(n)

for (i in seq_len(n)) {
  if (age[i] >= 16 & age[i] <= 20) {
    TimeHere[i] <- sample(1:3, 1, prob = c(0.5, 0.3, 0.2))
    
  } else if (age[i] > 20 & age[i] <= 36) {
    TimeHere[i] <- sample(
      1:6, 1,
      prob = c(0.30, 0.25, 0.18, 0.12, 0.10, 0.05)
    )
    
  } else if (age[i] > 35 & age[i] <= 45) {
    TimeHere[i] <- sample(
      3:8, 1,
      prob = c(0.25, 0.22, 0.18, 0.15, 0.10, 0.07)
    )
    
  } else {
    probs <- rev(seq_len(13))
    probs <- probs / sum(probs)
    TimeHere[i] <- sample(3:15, 1, prob = probs)
  }
}


# Screen time (hours/day)
# Base mean ~4
# - higher in men
# - higher at younger ages
screen_time <- 4 +
  rnorm(n, 0, 1.2) +
  0.5 * (sex == 1) -                 # men slightly higher
  0.03 * (age - 40)                  # younger -> more screen

screen_time <- pmin(pmax(screen_time, 0), 11)

# Sleep (hours/night)
# Negatively correlated with screen time
# Mean around 7, range 4–10
sleep <- 7 -
  0.35 * (screen_time - mean(screen_time)) +
  rnorm(n, 0, 0.8)

sleep <- pmin(pmax(sleep, 4), 10)


# Latent distress / well-being signals driven by screen time
# (used only to bias item probabilities)
distress_signal <- scale(screen_time)[, 1]

# PHQ-4 items (0–3, higher = worse)
# Slightly higher with more screen time
phq_items <- replicate(4, {
  raw <- round(
    1.2 +
      0.4 * distress_signal +
      rnorm(n, 0, 0.8)
  )
  pmin(pmax(raw, 0), 3)
})

colnames(phq_items) <- paste0("PHQ4_item", 1:4)

# WHO-5 items (1–5, higher = better)
# Lower with more screen time
who_items <- replicate(5, {
  raw <- round(
    3.8 -
      0.4 * distress_signal +
      rnorm(n, 0, 0.9)
  )
  pmin(pmax(raw, 1), 5)
})

colnames(who_items) <- paste0("WHO5_item", 1:5)

# Assemble dataset
data <- data.frame(
  age = age,
  sex = sex,
  survey = survey,
  TimeHere = TimeHere,
  position = position,
  screen_time = round(screen_time, 1),
  sleep = round(sleep, 1),
  who_items,
  phq_items
)

# Optional total scores (useful for teaching)
data$WHO5_total <- rowSums(data[, grep("WHO5_item", names(data))])
data$PHQ4_total <- rowSums(data[, grep("PHQ4_item", names(data))])

# Quick sanity checks
cor(data$screen_time, data$sleep)
cor(data$screen_time, data$WHO5_total)
cor(data$screen_time, data$PHQ4_total)
cor(data$age, data$screen_time)

write.csv(data, "data/simdata1.csv")
