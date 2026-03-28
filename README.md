# About

This repository includes a Python example script is included to automate the of the wheel radius given test data. The data given is an aboslute distance traveled, along with the y-displacement measured after said total distance. 

# Estimating Vehicle Turning Radius from Lateral Drift

This method estimates a vehicle's turning radius using measured lateral
drift during straight-line travel tests.

The idea is to approximate the vehicle path as an **arc of a circle with
constant curvature**.

------------------------------------------------------------------------

# Variables

-   `s` --- distance traveled (meters)
-   `y` --- lateral displacement from the straight line (meters)
-   `R` --- turning radius (meters)

------------------------------------------------------------------------

# Small-Angle Approximation

For small heading angles, the lateral offset after traveling distance
`s` is approximately

y ≈ s² / (2R)

Solving for the turning radius:

R ≈ s² / (2y)

------------------------------------------------------------------------

# Turning Radius from Measurements

  Distance s (m)   Lateral y (m)   Radius R = s² / (2y)
  ---------------- --------------- ----------------------
  10.06            0.68            74.4 m
  10.95            0.26            230.5 m
  10.085           0.625           81.4 m
  10.085           0.425           119.7 m
  10.085           0.36            141.3 m

Average turning radius:

R ≈ 129 m

This suggests the vehicle follows roughly a **129‑meter radius circle**.

------------------------------------------------------------------------

# Equivalent Heading Change

Heading change over distance `s`:

θ = s / R

For approximately 10 meters traveled:

θ = 10 / 129\
θ = 0.0775 radians\
θ ≈ 4.4°

So the vehicle turns roughly **4--5° every 10 meters**.

------------------------------------------------------------------------

# Wheel Radius Ratio

If the vehicle track width is `W`:

R_inner = R − W/2\
R_outer = R + W/2

Wheel path radius ratio:

ratio = R_inner / R_outer

Example with track width = 1.6 m:

R_inner = 129 − 0.8 = 128.2\
R_outer = 129 + 0.8 = 129.8

ratio ≈ 0.988

Meaning the **inside wheel travels about 98.8% of the distance of the
outside wheel**.

------------------------------------------------------------------------
