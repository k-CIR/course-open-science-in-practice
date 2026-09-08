# Simulated dataset 3

[:material-download: Download dataset 3 (.zip)](https://www.dropbox.com/scl/fi/5abaio8sn2hfwz3fjr3ir/simulated-dataset-3.zip?rlkey=2mbt29dfv1urgpnfiy7qjwsxi&st=twe2hldv&dl=1){ .md-button download="simulated-dataset-3.zip" }

## Introduction
Cardiovascular disease is a leading cause of mortality in Sweden, with myocardial infarction (heart attack) accounting for a substantial proportion of acute hospital admissions. Time from symptom onset to treatment is a well-established predictor of outcome ([DeVon et al., 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2884185/)). 

This dataset contains individual-level data from a simulated population survey covering all 21 Swedish counties (län) over the period 2023–2025. The sample consists of approximately 19 000 individuals aged 45 and older, with sample sizes proportional to each county's population.

### Files
- **`simulated-dataset-3.csv`** - The dataset is provided as a single CSV file, each row represents one individual. 
- **`dataset-3-key-csv`** - Code key describing the included variables.

### Variables
- **county**: Swedish county code (integer), corresponding to the 21 Swedish counties.
- **sex**: "Male", "Female", or "Other".
- **birthdate**: Date of birth (YYYY-MM-DD). All individuals are 45 or older at the survey start date (2023-01-01).
- **height**: Height in centimetres.
- **weight**: Weight in kilograms.
- **physical_activity**: Self-reported physical activity level on a 1–5 scale (1 = very low, 5 = very high).
- **smoking**: Current smoking status ("Yes" or "No").
- **alcohol**: Estimated weekly alcohol consumption in grams.
- **bloodpressure**: Systolic and diastolic blood pressure reported as a formatted string (e.g. "128/82").

### Heart attack incidents
Individuals who experienced a heart attack during the survey period have values for the following variables; all others have `NA`:

- **incident_date**: Date of the heart attack (YYYY-MM-DD).
- **time_to_treat**: Time in hours from heart attack to treatment initiation. Right-skewed distribution reflecting real-world variation in emergency response times. Weakly correlated with county population density.
- **incident_outcome**: Ordinal severity scale from 1 (minor, full recovery) to 5 (fatal). Correlated with time to treatment, age at incident, BMI, and smoking status.
- **death_date**: Date of death (YYYY-MM-DD), populated only for cases with `incident_outcome = 5`. Most deaths occur within a few days of the incident.

