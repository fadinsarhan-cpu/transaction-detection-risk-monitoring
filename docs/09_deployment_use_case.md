# Deployment / Use Case

This project can be deployed as a decision support tool for anti‑money‑laundering teams. The proposed deployment architecture involves:

1. **Data ingestion**: Streaming transaction data from core banking systems into a secure processing environment.

2. **Feature engineering and model inference**: Applying the trained XGBoost model to incoming transactions in near real time and assigning a risk score.

3. **Alert generation**: Flagging high‑risk transactions and forwarding them to analysts for review.

4. **Dashboard**: Presenting aggregated risk metrics and individual transaction details in an interactive Power BI report. Analysts can filter by date, typology and other attributes and drill down to transaction‑level information.

5. **Feedback loop**: Analysts’ decisions on flagged transactions are stored and used to retrain the model periodically, ensuring that the system adapts to new patterns.

Such a system helps institutions comply with AML regulations by surfacing hidden patterns of illicit activity while minimising false positives.
