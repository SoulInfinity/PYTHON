#WAP TO PRINT EVEN LENGTH OF WORDS IN A STRING
n = input("Enter a string")
s = n.split(" ")
for i in s:
    if len(i) % 2 == 0:
        print(i)
