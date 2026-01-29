import pandas as pd
from sklearn.ensemble import IsolationForest
df = pd.read_csv("permit_reconciliation_output.csv")
print(df.head())
features = df[["dispatched_quantity", "allowed_quantity"]]
model = IsolationForest(
    n_estimators=100,
    contamination=0.2,  # assume ~20% anomalies
    random_state=42
)

df["anomaly_flag"] = model.fit_predict(features)
df["anomaly_status"] = df["anomaly_flag"].map({
    1: "Normal",
    -1: "Anomaly"
})

print(df[["permit_id", "dispatched_quantity", "anomaly_status"]].head())
print(df["anomaly_status"].value_counts())
df.to_csv("anomaly_detection_output.csv", index=False)
print("AI-based anomaly detection completed")
