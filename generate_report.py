import pandas as pd

# Load final output
df = pd.read_csv("final_governance_output.csv")

# Calculate summary numbers
total_permits = df["permit_id"].nunique()
total_vehicles = df["vehicle_id"].nunique()

permit_violations = (df["permit_status"] == "Violation").sum()
ai_anomalies = (df["anomaly_status"] == "Anomaly").sum()
route_deviations = (df["route_status"] == "Deviated").sum()

high_risk_cases = (df["final_risk"] == "High Risk").sum()
normal_cases = (df["final_risk"] == "Normal").sum()

# Create report text
report_text = f"""
AI-Enabled Liquor Supply Chain Governance – Summary Report
---------------------------------------------------------

Total permits analyzed        : {total_permits}
Total vehicles tracked        : {total_vehicles}

Permit violations detected    : {permit_violations}
AI-based anomalies detected   : {ai_anomalies}
Route deviations detected     : {route_deviations}

High risk cases identified    : {high_risk_cases}
Normal cases                  : {normal_cases}

Key Observations:
- Automated permit reconciliation helped identify over-dispatch cases.
- AI-based anomaly detection highlighted unusual dispatch behavior.
- GPS-based route analysis detected vehicles deviating from expected routes.
- High-risk cases require further inspection and enforcement action.

(This report is generated using simulated district-level data for POC purposes.)
"""

# Save report to file
with open("governance_summary_report.txt", "w") as file:
    file.write(report_text)

print("Governance summary report generated successfully.")
