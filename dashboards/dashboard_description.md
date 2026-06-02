## Dashboard Overview

The dashboards in this project are designed to provide business stakeholders
with clear and actionable insights into transaction patterns and risk
metrics.  They display summary statistics, interactive charts and tables
that allow users to drill down into flagged transactions and monitor key
indicators over time.

Key components of the dashboards include:

1. **Volume and value trends:** Line charts showing daily or weekly transaction
   volumes and values, highlighting anomalies or spikes.

2. **Risk heatmap:** A heatmap of risk scores across different regions or
   customer segments, enabling quick identification of high‑risk areas.

3. **Model performance:** Visualisations of precision, recall and ROC‑AUC
   metrics to illustrate how well the classification model is performing.

4. **Flagged transaction table:** An interactive table listing the top
   transactions flagged as suspicious, with filters for date ranges and
   transaction attributes.

To reproduce the dashboards, run the notebook
`notebooks/05_dashboard_preparation.ipynb` to prepare the data.  Then use
Plotly Dash or another BI tool to assemble the visualisations described
above.  Screenshots of completed dashboards should be saved in
`dashboards/dashboard_screenshots/`.
