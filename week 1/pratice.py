import math

a = float(input("Please input the 'a' value "))
b = float(input("Please input the 'b' value "))
c = float(input("Please input the 'c' value "))
d = float(input("Please input the 'd' value "))

x = (a / b) * (a / (c**2 + d**2))

print(f"{x:.4f}")