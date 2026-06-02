# Dashboard Design & Business Insights

## Dashboard Purpose

This dashboard supports AML‑style transaction monitoring, suspicious activity analysis, high‑risk account identification, model performance review, and management decision‑making.

## Dashboard File

The interactive Power BI dashboard is saved in `dashboards/Dashboard_Fadi.pbix`. If the file is included in this repository, you can open it directly. If it is missing or exceeds GitHub’s file size limits, it should be provided via Git Large File Storage (LFS) or delivered externally.

## Dashboard Pages

| Dashboard Page              | Purpose                                     | Suggested Visuals                                                                               | Business Insight                                                  |
| --------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Executive Overview          | High‑level risk summary for decision makers | KPI cards, suspicious transaction rate, total transaction amount, suspicious amount, trend line | Helps managers understand overall transaction risk exposure       |
| Transaction Risk Monitoring | Analyze suspicious transaction patterns     | Suspicious transactions by payment type, currency, bank, and time                               | Helps identify risky transaction channels and suspicious patterns |
| High‑Risk Accounts          | Identify risky senders and receivers        | Top sender accounts, top receiver accounts, risk bands, suspicious ratio                        | Helps analysts prioritize accounts for investigation              |
| Typology Analysis           | Understand suspicious behavior types        | Typology distribution, amount by typology, suspicious behavior categories                       | Helps identify common laundering or suspicious behavior patterns  |
| Model Performance           | Explain the machine learning value          | Confusion matrix, precision, recall, F1‑score, ROC/AUC, model comparison table                  | Helps evaluate whether the model is useful for risk detection     |
| Investigation Detail        | Analyst drill‑down page                     | Transaction‑level table with filters by date, account, currency, payment type, and risk band    | Helps analysts review suspicious transactions case by case        |

## Key Performance Indicators

| KPI                         | Why it matters                                    |
| --------------------------- | ------------------------------------------------- |
| Total transactions          | Overall monitored transaction volume              |
| Suspicious transactions     | Main AML/risk detection count                     |
| Suspicious transaction rate | Shows concentration of suspicious activity        |
| Total suspicious amount     | Shows possible financial exposure                 |
| High‑risk accounts          | Helps prioritize investigation work               |
| Top sender banks            | Identifies source‑side risk concentration         |
| Top receiver banks          | Identifies destination‑side risk concentration    |
| Suspicious by currency      | Supports currency risk monitoring                 |
| Suspicious by payment type  | Shows risky transaction channels                  |
| Model recall                | Measures ability to catch suspicious cases        |
| False positive rate         | Shows analyst workload caused by incorrect alerts |

## Business Value

The dashboard helps different stakeholders:

* **AML analysts** can drill down to investigate flagged transactions, typologies, and high‑risk accounts.
* **Compliance officers** use the dashboard to monitor regulatory exposure and document investigation outcomes.
* **Risk managers** track trends, suspicious volumes, and performance metrics to allocate resources effectively.
* **Executive decision makers** get a holistic view of risk levels and trends to support strategic decision making.

## Screenshot Location

Dashboard screenshots should be stored in:

`dashboards/dashboard_screenshots/`
