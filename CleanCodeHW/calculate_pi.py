import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1
INSIDE_CIRCLE_COUNT = 0
Y_RANGE = 1
Y_SQUARE_EXPONENT = 2


# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-Y_RANGE, Y_RANGE)
    if x**SQUARE_EXPONENT + y**Y_SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        INSIDE_CIRCLE_COUNT += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
PI_ESTIMATE = (INSIDE_CIRCLE_COUNT / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {PI_ESTIMATE}")
