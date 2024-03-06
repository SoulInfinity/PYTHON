# Write a python program to remove all duplicates from given string
def removeDuplicates(s, n):
    exists = {}
    index = 0
    ans = ""
    for i in range(0, n):
        if s[i] not in exists or exists[s[i]] == 0:
            s[index] = s[i]
            print(s[index], end='')
            index += 1
            exists[s[i]] = 1
str1 = input("Enter a string : ")
str2 = list(str1)
n = len(str2)
removeDuplicates(str2,n)