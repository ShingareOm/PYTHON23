import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

# Example usage:
radius = 5
area = calculate_circle_area(radius)
circumference = calculate_circle_circumference(radius)

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
