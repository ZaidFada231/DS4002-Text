# Model Results

This document outlines the results of various classifiers applied to the "English Music Lyrics from Five Music Genres" dataset. The following models were tested: Random Forest as our main model, with a Dummy Classifier and K-Nearest Neighbors (KNN) as our benchmarks, along with a Cross-Validation using a Random Forest for accuracy verification.

> Each model’s accuracy and performance metrics such as precision, recall, and F1-score are presented to assess the classification of song genres based on lyrics.

## Random Forest Classifier

**Accuracy**: 0.4558

| Metric    | Metal | Country | Pop   | Rap   | Rock  | Overall |
| --------- | ----- | ------- | ----- | ----- | ----- | ------- |
| Precision | 0.46  | 0.51    | 0.30  | 0.66  | 0.28  | 0.44    |
| Recall    | 0.56  | 0.55    | 0.25  | 0.69  | 0.23  | 0.46    |
| F1-score  | 0.50  | 0.53    | 0.28  | 0.68  | 0.25  | 0.45    |
| Support   | 20030 | 20044   | 20069 | 19866 | 19991 | 100000  |

### Classification Report (Macro Average)

- **Precision**: 0.44
- **Recall**: 0.46
- **F1-score**: 0.45

### Explanation:

- **Precision** is the proportion of true positive predictions out of all positive predictions. For example, rap had the highest precision at 0.66, meaning that 66% of the songs classified as rap were indeed rap songs.
- **Recall** refers to the proportion of true positives identified out of all actual positives. The highest recall was for rap at 0.69.
- **F1-score** is the harmonic mean of precision and recall. A higher F1-score indicates a better balance between precision and recall.
- **Support** is the number of true instances for each genre in the test set.

---
## Benchmarks

The benchmark models allow usto create a standard against which the performance of our previous model can be evaluated. In order to set realistic and achievable goals for improvement, the benchmark model must be simplistic in architectcure and features input into it. These models will be essential for driving future improvement and ensuring advancements in future iterations.

### Benchmark 1: Dummy Classifier

The Dummy Classifier is a simple model used as a baseline for comparison. It predicts based on the most frequent class, which helps assess whether more advanced models provide meaningful improvements.

**Accuracy**: 0.19866

| Metric    | Metal | Country | Pop   | Rap   | Rock  | Overall |
| --------- | ----- | ------- | ----- | ----- | ----- | ------- |
| Precision | 0.00  | 0.00    | 0.00  | 0.20  | 0.00  | 0.04    |
| Recall    | 0.00  | 0.00    | 0.00  | 1.00  | 0.00  | 0.20    |
| F1-score  | 0.00  | 0.00    | 0.00  | 0.33  | 0.00  | 0.07    |
| Support   | 20030 | 20044   | 20069 | 19866 | 19991 | 100000  |

---

### Benchmark 2: KNN Classifier

The K-Nearest Neighbors (KNN) Classifier assigns a class to a song based on the majority class of its nearest neighbors. In this case, 3 neighbors were used.

**Accuracy**: 0.30263

This model's accuracy is higher than the Dummy Classifier but still much lower than Random Forest

| Metric    | Metal | Country | Pop   | Rap   | Rock  | Overall |
| --------- | ----- | ------- | ----- | ----- | ----- | ------- |
| Precision | 0.24  | 0.23    | 0.22  | 0.71  | 0.22  | 0.32    |
| Recall    | 0.45  | 0.27    | 0.17  | 0.53  | 0.10  | 0.30    |
| F1-score  | 0.31  | 0.25    | 0.19  | 0.61  | 0.14  | 0.30    |
| Support   | 20030 | 20044   | 20069 | 19866 | 19991 | 100000  |

---

## Cross Validation Report

Cross-validation is used to evaluate the stability of the Random Forest Classifier by testing it on multiple subsets of the dataset. This helps ensure the model's performance is not overly dependent on the particular test set used.

### Fold 1

| Metric    | Metal | Country | Pop   | Rap   | Rock  | Overall |
| --------- | ----- | ------- | ----- | ----- | ----- | ------- |
| Precision | 0.46  | 0.51    | 0.31  | 0.66  | 0.28  | 0.44    |
| Recall    | 0.56  | 0.55    | 0.25  | 0.69  | 0.23  | 0.46    |
| F1-score  | 0.50  | 0.53    | 0.28  | 0.68  | 0.25  | 0.45    |
| Support   | 20030 | 20044   | 20069 | 19866 | 19991 | 100000  |

### Fold 2

| Metric    | Metal | Country | Pop   | Rap   | Rock  | Overall |
| --------- | ----- | ------- | ----- | ----- | ----- | ------- |
| Precision | 0.46  | 0.51    | 0.30  | 0.66  | 0.28  | 0.44    |
| Recall    | 0.57  | 0.55    | 0.25  | 0.70  | 0.22  | 0.46    |
| F1-score  | 0.51  | 0.53    | 0.27  | 0.68  | 0.25  | 0.45    |
| Support   | 20065 | 19999   | 19935 | 19905 | 20096 | 100000  |

---

### Mean Accuracy across 5 folds: 0.4577

### Explanation:

- Cross-validation ensures that the model’s accuracy is not biased by a particular train-test split. It provided a more reliable assessment of a model's performance by incorporating all of the data, rather than a random subset. For future model iterations, it provides a clearer image of how hyperparamters (number of trees, max depth, class weight, etc.) affect performance The accuracy is consistent across the folds, with an average of 0.4577, which reinforces the findings from the Random Forest Classifier’s initial test.
