#WAP TO ENTER A STRING IS SYMMETRICAL OR PALINDROME
def isPalindrome(s):
    return s == s[::-1]

input_string = input("Enter a string")
if isPalindrome(input_string):
    print("Yes",input_string,"is palindrome")
else:
    print("No",input_string,"is not palindrome")

