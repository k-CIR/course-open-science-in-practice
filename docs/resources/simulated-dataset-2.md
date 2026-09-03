# Simulated dataset 2 - Working memory + EEG

[:material-download: Download dataset 2 (.zip)](https://www.dropbox.com/scl/fi/de0m9vnig7euqewtl149x/simulated-dataset-2.zip?rlkey=wma3oyvzpvlkd3esnh4t3j6si&st=9okj1gg5&dl=1){ .md-button download="simulated-dataset-2.zip" }

## Introduction
Working-memory (WM) training programs are sometimes proposed as a way to improve cognitive control, and [studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC8413785/) combining behavioral testing with EEG have looked for corresponding changes in event-related brain potentials such as the P300, which is thought to index attentional/updating processes recruited by tasks like the n-back. Here, 30 healthy participants completed a sequential n-back task in the lab while EEG was recorded, then practiced the task at home for roughly 10 minutes a day over a 14-day period, before returning to the lab to repeat the task a second time.

The data presentation in lecture 2 describe the data and show some potential analysis that can be performed using the data. You find those slides [here](placeholder).

## Description

### The n-back task
On each trial, a single digit (0–9) is shown on screen. Participants press a button whenever the digit currently shown is the same as the digit shown *n* positions earlier in the sequence (a "target"); otherwise they withhold the response ("nontarget"). For example, in an n = 4 block the sequence `1, 2, 5, 6, 3, 2, 4, 3, ...` contains a target at the second `2`, because it repeats the digit from 4 positions back.

Time zero in the epoched EEG data correspond to when the target is shown on screen, or in the case of no-target trials the nth digit.

For every trial, the file records which digit was shown, whether it was a true n-back match ("target"), whether the participant pressed the button, whether the response was correct, and the reaction time (for trials with a response).

## Files
- **`dataset-2-key.xlsx`** - Overview of all variables in the dataset.
- **`group_data.csv`** - group level data of age, sex and number of training days completed.

EEG and behaviour data files are stored in pseudo [BIDS](https://bids.neuroimaging.io/index.html) format as: `subject/session`

- **`sub-xx/ses-xx/sub-xx_ses-xx_task-nback_behav.csv`** - Behaviour (n-back task response) data per subject and session. Match `trial_id` with EEG data per subject and session.
- **`sub-xx/ses-xx/sub-xx_ses-xx_task-nback_eeg.csv`** - EEG data per subject and session. 1 ms resolution beween -100 and 800 ms relative target/no-target onset. First column is trial ID where n3_14 is the 14th trial in the n-back task with the target in position 3.
