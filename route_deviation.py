import pandas as pd
import numpy as np
gps = pd.read_csv("preprocessed_gps.csv")
print(gps.head())
REF_LAT = 16.50
REF_LON = 80.60
gps["distance_from_route"] = np.sqrt(
    (gps["latitude"] - REF_LAT)**2 +
    (gps["longitude"] - REF_LON)**2
)
DEVIATION_THRESHOLD = 0.2
gps["route_status"] = np.where(
    gps["distance_from_route"] > DEVIATION_THRESHOLD,
    "Deviated",
    "Normal"
)

print(gps[["vehicle_id", "distance_from_route", "route_status"]].head())
vehicle_route_status = gps.groupby("vehicle_id")["route_status"] \
    .apply(lambda x: "Deviated" if "Deviated" in x.values else "Normal") \
    .reset_index()

print(vehicle_route_status.head())
vehicle_route_status.to_csv("route_deviation_output.csv", index=False)
print("Route deviation analysis completed")
