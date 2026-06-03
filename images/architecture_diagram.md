# Deployment Architecture Diagram

Raw Transactions → ETL/Cleaning → Feature Engineering → ML Risk Scoring → Power BI Dashboard → AML Analyst Review

## Explanation

| Stage               | Description                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| **Raw Transactions**    | Source transaction records from banking systems or datasets                                      |
| **ETL/Cleaning**        | Standardises data, handles missing values, removes duplicates, and prepares the dataset          |
| **Feature Engineering** | Creates risk indicators such as suspicious ratios, amount bands, and account‑level risk features |
| **ML Risk Scoring**     | Uses classification models to estimate suspicious transaction probability                        |
| **Power BI Dashboard**  | Presents KPIs, trends, risk patterns, and flagged transactions                                   |
| **AML Analyst Review**  | Supports investigation, escalation, and compliance decision‑making                               |

> **Note:** A simple PNG diagram showing the same flow should be added to this folder if available.  Due to environment restrictions, it is not included here.