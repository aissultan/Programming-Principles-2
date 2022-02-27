import math

num_sides = int(input("Input number of sides: "))
s_length = float(input("Input the lenth of a side: "))

p_area = num_sides * (s_length ** 2) / (4 * math.tan(math.pi / num_sides))

print("The area of the polygon is:", round(p_area))