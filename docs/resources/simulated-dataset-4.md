# Simulated dataset 4

[:material-download: Download dataset 4 (.zip)](https://www.dropbox.com/scl/fi/t79fo64f2guqapi0bngh6/simulated-dataset-4.zip?rlkey=h2dyhy2hon3v1kfemxn8t288y&st=qo6c2dhb&dl=1){ .md-button download="simulated-dataset-4.zip" }

### Introduction
Chronotype is an individual's preference for sleep and activity timing and varies substantially across populations. It is influenced by both biological factors (age, sex) and environmental ones, including latitude and light exposure ([Roenneberg, et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23604485/)). Populations living at lower latitudes tend to show a later social timing of sleep, a phenomenon linked to cultural schedules and reduced seasonal variation in daylight ([Taillard, et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33545116/)). This dataset contains sleep data (actigraphy-derived sleep efficiency) and chronotype questionnaire scores collected from adults in Sweden and Spain using a similar survey protocol in both locations.

Tendency to be a morning-person or an evening-person is measured by the Morningness-Eveningsness Questionnaire [(MEQ; pdf)](https://www.med.upenn.edu/cbti/assets/user-content/documents/Morningness-Eveningness%20Questionnaire.pdf) developed by [Horne & Östberg, 1976](https://pubmed.ncbi.nlm.nih.gov/1027738/).

### Files
- **`simulated-dataset-4-sweden.csv`** - Data for participants recruited in [Spain](https://en.wikipedia.org/wiki/Spain).
- **`simulated-dataset-4-spain.csv`** - Data for participants recruited in [Sweden](https://www.ikea.com/se/sv/).
- **`dataset-4-spain-key.csv`** - Detailed description of variables in Spain dataset.
- **`dataset-4-sweden-key.csv`** - Detailed description of variables in Sweden dataset.

### Variables
- **id / participant_id**: Unique participant identifier.
- **age**: Age in years.
- **sex / gender**: Biological sex.
- **work_schedule / WorkSchedule**: Type of work schedule.
- **meq_score**: Total score on the Morningness-Eveningness Questionnaire ([Horne & Östberg, 1976](https://pubmed.ncbi.nlm.nih.gov/1027738/)).
- **sleep_onset**: Habitual sleep onset time in decimal hours (e.g. 23.5 = 23:30).
- **sleep_duration / SleepDuration**: Duration of sleep.
- **sleep_efficiency**: Actigraphy-derived sleep efficiency in percent (time asleep / time in bed × 100).
- **light_exposure**: Estimated daily light exposure in lux-hours, used as a proxy for outdoor time.
- **latitude**: Residential latitude in decimal degrees.
- **country**: Country of data collection ("Sweden" or "Spain").