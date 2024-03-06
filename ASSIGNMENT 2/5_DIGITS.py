number = input("Enter a 5-digit number: ")
if len(number) == 5 and number.isdigit():
    number = int(number)
    print("Digits at odd locations:")
    print("1st digit:", number // 10000 % 10)
    print("3rd digit:", number // 100 % 10)
    print("5th digit:", number % 10)
else:
    print("Please enter a valid 5-digit number.")
