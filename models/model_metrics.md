# Model Metrics

This document summarises the results of the classification models trained to detect
suspicious transactions in the **Transaction Detection & Risk Monitoring** project.
The goal of modelling is to flag potential money‑laundering activity while keeping
false positives at a manageable level for analysts.

## Dataset and Objective

The models were trained on the cleaned dataset
`data/processed/SAML-D_clean_optimized.csv` (about 633 k transactions).  The
target column, **`Is_laundering`**, marks each transaction as suspicious (`1`) or
normal (`0`).  The objective is a binary classification problem: maximise the
detection of suspicious transactions (high recall) while minimising the burden
of unnecessary alerts (false positives).

## Models Evaluated

The following algorithms were trained using the notebook
[`notebooks/04_machine_learning.ipynb`](../notebooks/04_machine_learning.ipynb):

* **Baseline model** – a majority‑class classifier that always predicts
  the most common class.  This provides a very low bar for comparison.
* **Logistic Regression** – a linear model fitted with class weights to
  compensate for extreme class imbalance.  Categorical features are
  one‑hot encoded and numeric fields are passed through unchanged.
* **Random Forest** – an ensemble of decision trees that can capture
  nonlinear relationships.  Class weights are again used to emphasise the
  minority (suspicious) class.
* **XGBoost** – a gradient‑boosted tree model.  It was not run in this
  evaluation due to dependency constraints but is available as an
  extension.

## Model Comparison

The table below summarises key evaluation metrics.  These values were
generated on a stratified sample of the processed dataset.  To update
them, rerun `04_machine_learning.ipynb` on the full dataset and write
the results to `models/model_comparison.csv`.

| Model               | Accuracy | Precision | Recall | F1‑score | ROC‑AUC | Notes                                        |
| ------------------- | -------: | --------: | -----: | -------: | ------: | -------------------------------------------- |
| **Baseline Model**      | 0.9989 | 0.0000    | 0.0000 | 0.0000    |    –   | Always predicts the majority class            |
| **Logistic Regression** | 0.8350 | 0.0036    | 0.5455 | 0.0072    | 0.7405 | High recall but extremely low precision       |
| **Random Forest**       | 0.9982 | 0.0784    | 0.0606 | 0.0684    | 0.5499 | Better precision but low recall               |
| **XGBoost**             |   –    |    –      |   –    |    –      |    –   | Not run in this evaluation                    |

## Confusion Matrix Interpretation

For the logistic regression model, the confusion matrix on a held‑out
test set (100 k sample) was:

* **True Positives:** 36 – suspicious transactions correctly flagged.
* **False Positives:** 9 869 – normal transactions incorrectly flagged.
* **True Negatives:** 50 065 – normal transactions correctly ignored.
* **False Negatives:** 30 – suspicious transactions missed.

This illustrates the trade‑off inherent in imbalanced classification.
While the model captures a majority of suspicious transactions (recall
≈ 0.55), the extremely low precision means that most alerts are false
positives.  Such a model would overwhelm analysts with unnecessary
investigations.

## Business Interpretation

For anti‑money‑laundering (AML) teams, **recall** is paramount because
missing a suspicious transaction carries significant regulatory and
financial risk.  However, a very low precision (high false positive
rate) places a heavy burden on investigators.  The logistic regression
model prioritises recall at the expense of precision, whereas the
random forest model achieves a better balance but still misses many
suspicious cases.  Stakeholders should tune models and decision
thresholds to achieve an acceptable trade‑off based on the
organisation’s risk appetite.

## Limitations and Next Steps

* **Class imbalance:** The extreme rarity of suspicious transactions
  makes it challenging to achieve both high recall and precision.
  Techniques such as SMOTE or adjusted class weights help but do not
  fully solve the problem.
* **Feature engineering:** Only a subset of available fields was used
  in this evaluation.  Incorporating additional features (e.g., account
  history, typology codes, transaction time patterns) may improve
  performance.
* **Model selection:** More advanced algorithms like XGBoost or LightGBM
  could offer better recall/precision trade‑offs.  Future work should
  experiment with these models and hyper‑parameter tuning.
* **Data drift:** Suspicious behaviour evolves over time.  Models need
  ongoing retraining and monitoring to remain effective.

These metrics are illustrative.  For the final project submission,
you should run the full pipeline, update the results here and include
confusion matrix and feature importance images in
`images/model_results/`.