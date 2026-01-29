import pandas as pd
import numpy as np

# Load Datasets
permits = pd.read_csv("permits.csv")
dispatch = pd.read_csv("dispatch.csv")
gps = pd.read_csv("gps.csv")

# Initial Data Exploration
print("Permits Data:")
print(permits.head())

print("\nDispatch Data:")
print(dispatch.head())

print("\nGPS Data:")
print(gps.head())

# Check for Missing Values
print("\nMissing Values in Permits:")
print(permits.isnull().sum())

print("\nMissing Values in Dispatch:")
print(dispatch.isnull().sum())

print("\nMissing Values in GPS:")
print(gps.isnull().sum())

# Check for Duplicate Records
print("\nDuplicate Records Count:")
print("Permit duplicates:", permits.duplicated().sum())
print("Dispatch duplicates:", dispatch.duplicated().sum())
print("GPS duplicates:", gps.duplicated().sum())


# Merge Dispatch and Permit Data
merged_df = pd.merge(
    dispatch,
    permits,
    on="permit_id",
    how="left"   # Keep all dispatch records
)

print("\nMerged Data Preview:")
print(merged_df.head())


# Feature Engineering
# Calculate difference between dispatched and allowed quantity
merged_df["quantity_difference"] = (
    merged_df["dispatched_quantity"] - merged_df["allowed_quantity"]
)

# Identify over-dispatch cases
merged_df["over_dispatch"] = merged_df["quantity_difference"] > 0

# Assign permit status based on dispatch behavior
merged_df["permit_status"] = np.where(
    merged_df["over_dispatch"],
    "Violation",
    "Normal"
)

print("\nPermit Status Sample:")
print(merged_df[["permit_id", "permit_status"]].head())



# GPS Data Processing
# Convert timestamp column to datetime format
gps["timestamp"] = pd.to_datetime(gps["timestamp"])

# Count number of GPS points per vehicle
gps_counts = gps.groupby("vehicle_id").size().reset_index(name="gps_points")

print("\nGPS Points Count per Vehicle:")
print(gps_counts.head())


# Save Preprocessed Data
merged_df.to_csv("preprocessed_permit_dispatch.csv", index=False)
gps.to_csv("preprocessed_gps.csv", index=False)

print("\nPreprocessed files saved successfully")
