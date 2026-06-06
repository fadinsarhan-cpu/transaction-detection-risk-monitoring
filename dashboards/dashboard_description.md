# Dashboard Description

The **Transaction Detection & Risk Monitoring** dashboard is designed to give
business stakeholders a clear, actionable view of transaction activity and
associated risk.  Each page targets a specific audience and decision‑making
need.  Screenshots of the final dashboards should be stored in
`dashboards/dashboard_screenshots/` (see file names below).  If the Power BI
file (`Dashboard_Fadi.pbix`) is too large for GitHub, download it
separately or use Git LFS; it is not included in this repository by default.

## A. Executive Overview

**Purpose:** Provide a high‑level summary of transaction volume, risk and
overall AML performance for managers and executives.

**Suggested visuals:**

- **KPI cards** summarising:
  - Total transactions
  - Suspicious transactions
  - Suspicious transaction rate
  - Total suspicious amount
- **Transaction trend line** to show volume over time and highlight spikes.

Screenshot: `01_executive_overview.png`

## B. Transaction Risk Monitoring

**Purpose:** Analyse patterns in suspicious transactions to understand
where and how risk is concentrated.

**Suggested visuals:**

- Suspicious transactions by payment type
- Suspicious transactions by currency
- Suspicious transactions by sender bank (if available)
- Suspicious transactions by receiver bank (if available)
- Suspicious transactions over time (daily/weekly/monthly)

Screenshot: `02_transaction_risk.png`

## C. High‑Risk Accounts

**Purpose:** Identify accounts that require further investigation.

**Suggested visuals:**

- Top sender accounts by suspicious activity
- Top receiver accounts by suspicious activity
- Risk bands (Low, Medium, High) summarising account‑level risk
- Suspicious ratio per account (suspicious transactions / total transactions)

Screenshot: `03_high_risk_accounts.png`

## D. Typology Analysis

**Purpose:** Understand the types of suspicious behaviour detected by the
models and rules.

**Suggested visuals:**

- Distribution of typologies if a typology column exists
- Total amount by typology to gauge financial impact
- Suspicious transactions by behavioural category

## E. Model Performance

**Purpose:** Demonstrate the value of advanced analytics and the efficacy of
the classification models.

**Suggested visuals:**

- Confusion matrix highlighting true positives, false positives, etc.
- Precision, recall and F1‑score charts
- ROC/AUC curves if available
- Model comparison table summarising evaluation metrics

Screenshot: `04_model_performance.png`

## F. Investigation Detail

**Purpose:** Provide analysts with a detailed view of each suspicious
transaction and allow interactive filtering.

**Suggested visuals:**

- Transaction‑level table with drill‑down capability
- Filters for date range, account, payment type, currency, risk band and
  prediction result

## KPI Table

The table below summarises the key performance indicators (KPIs) used in the
dashboards and explains why each metric is important.

| KPI                         | Why it matters                                                |
| --------------------------- | ------------------------------------------------------------- |
| **Total transactions**      | Overall monitored volume, providing context for risk metrics. |
| **Suspicious transactions** | Main AML/risk detection count.                                |
| **Suspicious transaction rate** | Shows the concentration of suspicious behaviour relative to overall volume. |
| **Total suspicious amount** | Indicates potential financial exposure due to suspicious activity. |
| **High‑risk accounts**      | Helps prioritise investigations on the most risky customers.   |
| **Top sender banks**        | Identifies concentration of risk on the payment origin side.   |
| **Top receiver banks**      | Identifies concentration of risk on the destination side.      |
| **Suspicious by currency**  | Supports currency‑specific risk monitoring and FX exposure.    |
| **Suspicious by payment type** | Highlights which transaction channels are most risky.       |
| **Model recall**            | Measures how effectively the model captures actual suspicious cases. |
| **False positive rate**     | Indicates analyst workload caused by incorrect alerts.         |
