import math

def triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input sides of the first triangle
a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))

# Input sides of the second triangle
a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))

# Calculate the areas of both triangles
area1 = triangle_area(a1, b1, c1)
area2 = triangle_area(a2, b2, c2)

# Calculate the total area
total_area = area1 + area2

# Calculate the contribution of each triangle to the total area
contribution1 = (area1 / total_area) * 100
contribution2 = (area2 / total_area) * 100

# Print the results
print(f"\nArea of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"First triangle's contribution to the total area: {contribution1:.2f}%")
print(f"Second triangle's contribution to the total area: {contribution2:.2f}%")
