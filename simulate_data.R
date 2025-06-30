
require(pacman)

pacman::p_load(
    'dplyr',
    'readr'
)

# Simulate dataset with same structure as dfs
set.seed(123)

n_subjects <- 52

dfs_sim <- expand.grid(
    subject = paste0("sub-", sprintf("%02d", 1:n_subjects)),
    # etc...
) %>%
    mutate(
    depression = rnorm(n(), mean = 10, sd = 3),
     # etc...
    ) %>% as_tibble()

write_tsv(dfs_sim, 'simulated_data.tsv')