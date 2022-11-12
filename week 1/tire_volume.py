import math
from turtle import width

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (( math.pi * width**2 * aspect_ratio * ( width * aspect_ratio + 2540 * diameter)) / 10000000000 )

print(f"The approximate volume is {tire_volume:.2f} liters")