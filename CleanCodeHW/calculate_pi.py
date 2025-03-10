import random

# Simulation parameters
CIRCLE_RADIUS = 1
TOTAL_SIMULATION_POINTS = 1000000
CIRCLE_TO_SQUARE_RATIO = 4
SQUARE_POWER = 2
POINT_IN_CIRCLE_INCREMENT = 1
POINTS_IN_CIRCLE = 0
COORDINATE_RANGE = 1

# Randomly generate points and count those inside the circle
for _ in range(TOTAL_SIMULATION_POINTS):
    point_x = random.uniform(-CIRCLE_RADIUS, CIRCLE_RADIUS)
    point_y = random.uniform(-COORDINATE_RANGE, COORDINATE_RANGE)
    if point_x**SQUARE_POWER + point_y**SQUARE_POWER <= CIRCLE_RADIUS**SQUARE_POWER:
        POINTS_IN_CIRCLE += POINT_IN_CIRCLE_INCREMENT

# Estimate pi based on the number of points inside the circle
estimated_pi = (POINTS_IN_CIRCLE / TOTAL_SIMULATION_POINTS) * CIRCLE_TO_SQUARE_RATIO

print(f"Estimated value of pi is: {estimated_pi}")
