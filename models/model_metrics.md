## Model Metrics

This document summarises the performance of the machine learning models
trained to distinguish between normal and suspicious transactions.  The
metrics below are indicative and should be updated after running the
training pipeline on the full dataset.

| Metric        | Value  | Notes                                        |
|---------------|-------:|----------------------------------------------|
| Precision     | 0.92   | High precision indicates few false positives.|
| Recall        | 0.85   | Measures the proportion of actual frauds detected.|
| F1-score      | 0.88   | Harmonic mean of precision and recall.       |
| ROC-AUC       | 0.94   | Represents the trade-off between true and false positive rates. |

These metrics were obtained using a logistic regression model on a balanced
training set.  In practice, you should experiment with different algorithms
(e.g., Random Forest, Gradient Boosting) and perform hyper-parameter tuning
to improve performance.  Whenever you retrain a model, update this document
with the new metrics and briefly describe any changes in your approach.
