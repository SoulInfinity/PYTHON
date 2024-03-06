import cmath
a = int(input("Enter the value for a"))
b = int(input("Enter the value for b"))
c = int(input("Enter the value for c"))
d = (b**2) - (4*a*c)

e = (-b-cmath.sqrt(d))/(2*a)
f = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(e,f))
