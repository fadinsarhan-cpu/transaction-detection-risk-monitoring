# Advanced Analytics and AI Modeling

Statistical tests and machine‑learning models were developed in `03_statistical_analysis.ipynb` and `04_machine_learning.ipynb`. Highlights include:

- **Statistical analysis**: We evaluated summary statistics and performed hypothesis tests to compare normal and suspicious transactions. Techniques such as t‑tests, chi‑square tests and correlation analysis helped identify discriminative features.

- **Model selection**: Several classification algorithms were assessed, including logistic regression, random forest, gradient boosting and extreme gradient boosting (XGBoost). We also experimented with resampling techniques from the `imbalanced-learn` library to address the class imbalance.

- **Evaluation metrics**: Because the dataset is imbalanced, we focused on recall and area under the ROC curve (AUC) rather than overall accuracy. The best performing model, XGBoost, achieved a recall of 0.92 for suspicious transactions and an AUC of 0.98 on a held‑out test set.

- **Feature importance**: Tree‑based models provided insight into the most influential variables. Transaction amount, transaction type and certain typology codes were among the top predictors.

The final model is saved in the `models/` directory and can be loaded for inference.
