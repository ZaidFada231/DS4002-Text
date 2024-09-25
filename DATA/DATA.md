# Data Appendix

This appendix provides an overview of the datasets used in this project, detailing the structure and content of the data, including descriptive statistics and variable explanations.

## 1. Dataset Overview

### Dataset Title:

**English Music Lyrics from Five Music Genres**

### Source:

The dataset is from Kaggle, available [here](https://www.kaggle.com/datasets/d3stron/english-music-lyrics-5-genres-500k/data).

### Unit of Observation:

Each row in the dataset represents a unique song, with its lyrics and associated genre.

### Dataset Description:

The dataset includes 500,000 rows of song lyrics across five music genres: Country, Metal, Rock, Pop, and Rap. It is split into two main files: `cleaned_train_lyrics` and `cleaned_test_lyrics`, both containing the same structure but used for training and testing in the project.

### Dataset Structure:

- **File 1:** `cleaned_train_lyrics`
- **File 2:** `cleaned_test_lyrics`

## 2. Variables

Each dataset contains the following variables:

### 2.1 Genre

- **Description:** This variable represents the music genre of each song in the dataset.
- **Data Type:** Categorical
- **Possible Values:**
  - `Country`
  - `Metal`
  - `Rock`
  - `Pop`
  - `Rap`
- **Example:** For a country song like "Ring of Fire" by Johnny Cash, the genre would be labeled as `Country`.

### 2.2 Lyrics

- **Description:** Contains the lyrics of the song in English.
- **Data Type:** Text
- **Example:** "Can you hear me call your name. I'm not far away."

## 3. Data Cleaning and Preprocessing

The following steps were applied to clean and preprocess the data:

1. **Common Word Removal:** Common words (e.g., "the," "and") were removed to help classification accuracy.
2. **Lowercasing:** All text was converted to lowercase for simplicity.

## 4. Data Summary

### 4.1 Summary Statistics

| Variable | Number of Unique Values | Min Length | Max Length   |
| -------- | ----------------------- | ---------- | ------------ |
| Genre    | 5                       | N/A        | N/A          |
| Lyrics   | 500,000                 | 1 word     | 3,000+ words |

## 5. Steps to Access this Data

1. Visit https://www.kaggle.com/datasets/d3stron/english-music-lyrics-5-genres-500k/data
2. Click black download button in top right corner
3. Download folder
4. Unzip the 2 files included, `cleaned_test_lyrics` and `cleaned_train_lyrics` and place them both into the `/DATA` folder so that the file structure is:
   - `\Data`
     - `cleaned_test_lyrics`
     - `cleaned_train_lyrics`
5. All scripts will run based on this relative path to the `cleaned_train_lyrics`
