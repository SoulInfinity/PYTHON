# 3. WAP to create an integer list of 20 elements increase the odd valued elements by 5.

lst = list(range(1, 21))
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[i] += 5
print(lst)

