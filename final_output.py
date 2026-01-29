import pandas as pd
import numpy as np
permit_df = pd.read_csv("anomaly_detection_output.csv")
route_df = pd.read_csv("route_deviation_output.csv")

print(permit_df.head())
print(route_df.head())

final_df = pd.merge(
    permit_df,
    route_df,
    on="vehicle_id",
    how="left"
)

print(final_df.head())
final_df["final_risk"] = np.where(
    (final_df["permit_status"] == "Violation") |
    (final_df["anomaly_status"] == "Anomaly") |
    (final_df["route_status"] == "Deviated"),
    "High Risk",
    "Normal"
)
print(final_df[
    ["permit_id", "vehicle_id", "permit_status", "anomaly_status", "route_status", "final_risk"]
].head())
final_df.to_csv("final_governance_output.csv", index=False)
print("Final governance output generated")
