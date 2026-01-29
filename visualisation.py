import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("final_governance_output.csv")
print(df.head())
risk_counts = df["final_risk"].value_counts()

risk_counts.plot(kind="bar")
plt.title("Final Risk Classification")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.show()
reason_counts = {
    "Permit Violations": (df["permit_status"] == "Violation").sum(),
    "AI Anomalies": (df["anomaly_status"] == "Anomaly").sum(),
    "Route Deviations": (df["route_status"] == "Deviated").sum()
}

pd.Series(reason_counts).plot(kind="bar")
plt.title("Reasons for Risk Detection")
plt.ylabel("Count")
plt.show()
