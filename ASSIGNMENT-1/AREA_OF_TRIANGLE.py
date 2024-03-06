import math

a = float(input("Enter one side"))
b = float(input("Enter another side"))
c = float(input("Enter third side"))
s = float((a+b+c)/2)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)