import pandas as pd
import numpy as np

# Load merged permit-dispatch data
df = pd.read_csv("preprocessed_permit_dispatch.csv")

print(df.head())

# Difference between dispatched and allowed
df["quantity_difference"] = df["dispatched_quantity"] - df["allowed_quantity"]

# Rule-based status
df["permit_status"] = np.where(
    df["quantity_difference"] > 0,
    "Violation",
    "Normal"
)
print(df[["permit_id", "allowed_quantity", "dispatched_quantity", "permit_status"]].head())

df.to_csv("permit_reconciliation_output.csv", index=False)
print("Permit reconciliation completed and saved")
