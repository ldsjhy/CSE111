# import math

# a = input("Please input the 'a' value ")
# b = input("Please input the 'b' value ")
# c = input("Please input the 'c' value ")
# d = input("Please input the 'd' value ")

# x = float((a / b) * (a / (c**2 + d**2)))

# print(f"{x:.4f}")



def compute_data(a, b, c, d):
    return (a / b) * (a / (c**2+d**2))
    
    # x = (a / b) * (a / (c**2+d**2))
    # return x

print(compute_data(5, 4, 3, 2) == 0.4807692307692308)
print(compute_data(9, 1, 4, 6) == 1.5576923076923077)

# print(f"{value:.4f}")

