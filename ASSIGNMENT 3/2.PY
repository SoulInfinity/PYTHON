#WAP TO FIND THE FACTORIAL OF A NUMBER
def factorial(n):
    if n < 0:
        print("No factorial for negetive numbers")
    elif n == 0:
        print("The factorial of the number is ",n)
    else:
        return n*factorial(n-1)
num = int(input("Enter the number for finding factorial"))
print("Factorial of ",num,"is",factorial(num))
