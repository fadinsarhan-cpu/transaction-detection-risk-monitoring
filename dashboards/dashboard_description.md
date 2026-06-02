# Dashboard Design & Business Insights

## Dashboard Purpose

This dashboard supports AML-style transaction monitoring by providing a consolidated view of suspicious activity, high-risk accounts and model performance.  It helps analysts and managers identify patterns, prioritise investigations and make data-driven decisions.

## Dashboard File

The interactive Power BI dashboard is saved in `dashboards/Dashboard_Fadi.pbix`.  
Due to file size constraints it may not be tracked directly in this repository.  If the PBIX file is not present, provide it via Git LFS or as a separate deliverable.  The CSV exports and screenshots included here summarise its contents.

## Dashboard Pages

| Dashboard Page              | Purpose                                     | Suggested Visuals                                      | Business Insight                                                 |
| --------------------------- | ------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| Executive Overview          | High-level risk summary for decision makers | KPI cards, suspicious rate, total amount, trend line   | Helps managers understand overall transaction risk exposure      |
| Transaction Risk Monitoring | Analyse suspicious transaction patterns     | Suspicious by payment type, currency, bank, and time   | Identifies risky channels, currencies and patterns               |
| High-Risk Accounts          | Identify risky senders and receivers        | Top accounts, risk bands, suspicious ratio             | Helps analysts prioritise accounts for investigation             |
| Typology Analysis           | Understand suspicious behaviour types        | Typology distribution, amount by typology              | Highlights common laundering or suspicious behaviour patterns    |
| Model Performance           | Explain the machine-learning value          | Confusion matrix, precision, recall, F1-score, ROC/AUC | Evaluates whether the model is useful for risk detection         |
| Investigation Detail        | Analyst drill-down page                     | Transaction table with filters                         | Supports case-by-case review of suspicious transactions          |

## Key Performance Indicators

| KPI                         | Why it matters                                    |
| --------------------------- | ------------------------------------------------- |
| Total transactions          | Overall monitored transaction volume              |
| Suspicious transactions     | Main AML/risk detection count                     |
| Suspicious transaction rate | Shows concentration of suspicious activity        |
| Total suspicious amount     | Indicates potential financial exposure            |
| High-risk accounts          | Helps prioritise investigation work               |
| Top sender banks            | Identifies source-side risk concentration         |
| Top receiver banks          | Identifies destination-side risk concentration    |
| Suspicious by currency      | Supports currency-specific risk monitoring        |
| Suspicious by payment type  | Highlights risky payment channels                 |
| Model recall                | Measures ability to catch suspicious cases        |
| False positive rate         | Indicates analyst workload due to incorrect alerts |

## Business Value

The dashboard supports multiple stakeholders:

* **AML analysts** can filter and drill down to investigate flagged transactions, typologies and high-risk accounts.
* **Compliance officers** use the dashboards to monitor regulatory exposure and document investigation outcomes.
* **Risk managers** track trends, suspicious volumes and performance metrics to allocate resources effectively.
* **Executives/management** gain a holistic view of risk levels and trends to support strategic decision making.

## Screenshots

Dashboard screenshots should be stored in `dashboards/dashboard_screenshots/` with the following filenames:

* `01_executive_overview.png`
* `02_transaction_risk.png`
* `03_high_risk_accounts.png`
* `04_model_performance.png`

Each screenshot should capture the corresponding page of the Power BI report with the visuals described above.
