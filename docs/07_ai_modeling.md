# Advanced Analytics and AI Modeling

This section documents the machine‑learning pipeline used to detect suspicious
transactions in the **Transaction Detection & Risk Monitoring** project.  It
explains the modelling objective, describes the techniques used to handle
class imbalance, summarises the models evaluated and interprets the results
from a business perspective.

## Modelling Objective

The goal is to build a classifier that predicts whether a given payment is
**suspicious** (`Is_laundering = 1`) or **normal** (`Is_laundering = 0`).
Identifying suspicious transactions early allows compliance teams to
investigate potential money‑laundering activities and minimise financial
exposure.  Since only a small fraction of transactions are suspicious, this
is an imbalanced **binary classification** problem.

## Why It’s a Classification Problem

Suspicious transaction detection involves assigning each transaction to one
of two categories: suspicious or normal.  The target variable
`Is_laundering` is therefore binary, making classification the appropriate
approach.  Regression models are not suitable because the output is not a
continuous quantity.

## Class Imbalance

In most real‑world AML datasets, the number of suspicious transactions is
much smaller than the number of normal transactions.  Class imbalance can
cause standard algorithms to favour the majority class and miss rare
positives.  We address this by:

- **Using class weights** in algorithms like Logistic Regression and
  Random Forest so that misclassifying suspicious cases incurs a higher cost.
- **Applying SMOTE (Synthetic Minority Over‑sampling Technique)** to
  generate synthetic suspicious examples and balance the training set.

## Models Used

The following models were evaluated in `notebooks/04_machine_learning.ipynb`
and `src/model_training.py`:

1. **Baseline model:** A dummy classifier (e.g., predicting the majority
   class) provides a performance benchmark.
2. **Logistic Regression:** A linear model suitable for binary
   classification; class weights are used to handle imbalance.
3. **Random Forest:** An ensemble of decision trees that captures
   non‑linear relationships; class weights and/or balanced subsampling
   improve its sensitivity to suspicious cases.
4. **XGBoost (if available):** A gradient boosted tree model that often
   achieves strong performance.  Installation of the `xgboost` package is
   optional; if available, it should be included and tuned.

## Evaluation Metrics

Because of the imbalanced nature of the problem, we emphasise **recall**
(also known as sensitivity or true positive rate) over accuracy.  The
following metrics are computed on a held‑out test set:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted suspicious transactions that are truly suspicious.
- **Recall:** Proportion of actual suspicious transactions detected by the model.
- **F1‑score:** Harmonic mean of precision and recall.
- **ROC‑AUC:** Area under the receiver operating characteristic curve, measuring the trade‑off between true and false positive rates.

## Model Comparison Results

The table below summarises the evaluation metrics for each model.  These
values should be updated after running the training pipeline on the full
dataset.  Refer to `models/model_metrics.md` for the latest metrics.

| Model               | Accuracy | Precision | Recall | F1‑score | ROC‑AUC | Notes                              |
| ------------------- | -------: | --------: | -----: | -------: | ------: | ---------------------------------- |
| **Baseline Model**      |   0.9989 |    0.0000 |  0.0000 |   0.0000 |    –   | Always predicts the majority class |
| **Logistic Regression** |   0.8350 |    0.0036 |  0.5455 |   0.0072 |  0.7405 | High recall but very low precision |
| **Random Forest**       |   0.9982 |    0.0784 |  0.0606 |   0.0684 |  0.5499 | Better precision but low recall    |
| **XGBoost**             |     –   |      –    |    –   |     –    |    –   | Not run in this evaluation        |

These values were computed on a sampled version of the processed dataset and are provided
for illustration.  See `models/model_metrics.md` for a more detailed discussion.

## Confusion Matrix

The confusion matrix provides a breakdown of correct and incorrect
predictions:

- **True Positives (TP):** Suspicious transactions correctly flagged.
- **False Positives (FP):** Normal transactions incorrectly flagged
  (analyst workload).
- **True Negatives (TN):** Normal transactions correctly ignored.
- **False Negatives (FN):** Suspicious transactions missed (risk exposure).

Minimising **FN** is critical because missing a suspicious transaction could
allow money laundering to go undetected.  However, a high number of **FP**
creates extra work for analysts.  Balancing recall and precision is thus
key.

## Feature Importance

Tree‑based models (Random Forest and XGBoost) can provide insights into
which features are most influential.  Commonly important features include
transaction amount, payment type, currency, typology codes and account
history.  Examining feature importance helps validate model behaviour and
improves interpretability.

## Model Limitations

- **Data quality:** Missing or inconsistent data can hinder model
  performance.  Ensure that the ETL process cleans and standardises input
  fields.
- **Evolving patterns:** Criminal behaviour changes over time; models need
  regular retraining to remain effective.
- **Limited interpretability:** Complex models like XGBoost provide less
  transparency than linear models.  Use SHAP or feature importance plots to
  explain decisions.

## Business Interpretation

For AML teams, **recall** is arguably the most important metric: catching
as many suspicious transactions as possible reduces the risk of
money‑laundering going undetected.  Precision matters too, because a high
false positive rate increases analyst workload and may desensitise teams to
alerts.  Stakeholders should select a model that offers a balanced trade‑off
between recall and precision based on the organisation’s tolerance for
false positives.

The model comparison and metrics documented here, along with the
confusion matrices and feature importance plots saved in
`models/model_metrics.md` and `images/model_results/`, provide evidence
that advanced analytics adds value to the risk‑monitoring process.