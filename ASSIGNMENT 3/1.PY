# WRITE A PROGRAM TO ENTER TWIN PRIME NUMBERS BETWEEN 1 TO N
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
def generate_twins(start,end):
    for i in range(start,end):
        j = i + 2
        if(is_prime(i) and is_prime(j)):
            print("{:d} and {:d}".format(i,j))
num = int(input("Enter a number"))
generate_twins(2,num)
