# write a python to enter percentage and display the gradation system
marks = int(input("Enter the marks of the student:"))
if marks >= 90:
    print("GRADE O")
elif marks >= 80:
    print("GRADE E")
elif marks >= 70:
    print("GRADE A")
elif marks >= 60:
    print("GRADE B")
elif marks >= 50:
    print("GRADE C")
elif marks >= 40:
    print("GRADE D")
else:
    print("Fail")
