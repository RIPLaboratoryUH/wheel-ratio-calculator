import numpy as np
import pandas as pd

# Your measurements: (distance_traveled, y_displacement)
data = [
    (10.06, 0.68),
    (10.95, 0.26),
    (10.085, 0.625),
    (10.085, 0.425),
    (10.085, 0.36)
]

df = pd.DataFrame(data, columns=["distance_m", "y_displacement_m"])

# Turning radius approximation
df["radius_m"] = df["distance_m"]**2 / (2 * df["y_displacement_m"])

# Heading change estimate
df["heading_change_rad"] = df["distance_m"] / df["radius_m"]
df["heading_change_deg"] = np.degrees(df["heading_change_rad"])

# Average radius
avg_radius = df["radius_m"].mean()

print("Computed values per trial:")
print(df)

print("\nAverage turning radius:", avg_radius, "meters")

# Optional: wheel radius ratio if you know track width
track_width = 1.6  # meters (change to your vehicle value)

R_inner = avg_radius - track_width/2
R_outer = avg_radius + track_width/2
ratio = R_inner / R_outer

print("\nWheel path radius ratio (inner/outer):", ratio)
