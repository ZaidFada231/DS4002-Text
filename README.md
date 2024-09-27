# Classification Model for Music Lyrics

**Group Leader**: Malek Thabet  
**Group Members**: Zaid Fada, Chris Woods  
**Course**: DS 4002  
**Date**: 27 September 2024

## Project Overview

This repository contains the code, data, and documentation for our project to classify musical genres based solely on lyrical data using an Random Forest classification model. Our goal is to achieve an accuracy of 75% or greater in genre classification using the “English Music Lyrics from Five Music Genres” dataset from Kaggle. The analysis will focus on feature extraction and model training to improve classification performance.

## Repository Structure

- **README.md**: Provides an overview and instructions for reproducing the results.
- **LICENSE.md**: License for the project (MIT License).
- **requirements.txt**: Python packages needed for the project
- **SCRIPTS/**: Contains the Python scripts for data processing, feature engineering, and model training.
- **DATA/**: Contains the dataset used for training and testing.
- **OUTPUT/**: Stores the results, including figures and tables from the analysis.

```bash
.
├── README.md                # Project overview and instructions
├── LICENSE.md               # License information (MIT)
├── requirements.txt         # Python packages needed for the project
├── SCRIPTS/
│   ├── exploratoryplots.ipynb  # Prelim data discobvery
│   └── analysis.ipynb       # Detailed step-by-step analysis performed
├── DATA/
│   └── Data.md              # Steps to download dataset
├── OUTPUT/
│   ├── model_results.md    # Accuracy, confusion matrix, and classification report
│   └── plots/              # Figures generated during prelim data discovery
```

## Software and Platform

- **Programming Language**: Python
- **Packages Required**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `seaborn`
  - `matplotlib`
  - `wordcloud`
- **Platform**: Windows, macOS, or Linux

## Data

The dataset used for this project is the "English Music Lyrics from Five Music Genres" dataset from Kaggle, which contains 500,000 song lyrics from five genres: country, metal, rock, pop, and rap.

## Instructions for Reproducing Results

1. Clone this repository:

   ```bash
   git clone [repository link]
   cd [repository directory]
   ```

2. Install the required Python packages: Ensure that Python 3.x is installed. Then, install the necessary packages by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and prepare the data:

   - Go to the `Data.md` and follow the steps to download our data
   - Place the dataset in the `DATA/` folder

4. Run the analysis:

   - Go to `/SCRIPTS/analysis.ipynb`, follow the comments in the cells and run each cell to perform our analysis!

5. Review the results:
   - The model’s accuracy, precision, recall, and other performance metrics will be saved in the [models_results.md](OUTPUTS/models_results.md) file
   - Visualizations, including the confusion matrix and other plots, will be saved in the `OUTPUTS/plots/` directory.
