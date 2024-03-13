import math
import os.path

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
x1, y1 = 4, 0
x2, y2 = 6, 6

result = calculate_distance(x1, y1, x2, y2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {result}")

print(os.path.abspath("sude1.py"))
print(os.path.dirname("sude1.py"))