import math

def compute_area(r):
    return math.pi * r * r

radius = float(input("Please enter a radius: "))

# print("The area is: " + compute_area(radius)) -->error
print(f"The area is: {compute_area(radius)}")