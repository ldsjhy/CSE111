import math
from turtle import width

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (( math.pi * width**2 * aspect_ratio * ( width * aspect_ratio + 2540 * diameter)) / 10000000000 )

print(f"The approximate volume is {tire_volume:.2f} liters")

purchase_or_not = input("Would you like to purchase this tire with this volume? please type 'yes or no' ")

if purchase_or_not.lower() == "yes":

    phone_number = input("Then, please type your phoen number for us to contact with you ")

elif purchase_or_not.lower() == "no":

    print("You're fine! Just let us know when you want to purchase it later.")

else:
    print("Please type 'yes or no'")

from datetime import datetime

current_date_and_time = datetime.now()

with open("volumes.txt", mode="at") as volume_file:

    print(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}")


    
