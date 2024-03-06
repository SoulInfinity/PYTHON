# WAP to create a function that prints the first n terms of the fibonacci series using without using recursion
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Enter a number"))
fibonacci(n)
