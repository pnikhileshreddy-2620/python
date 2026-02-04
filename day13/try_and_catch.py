

age=0
try:
    age = int(input("Enter the number "))
except ValueError:
    print("pls enter the number")
    age = int(input("Enter the number "))

if age>18:
    print("Eligible for driving the car")
else:
    print("Not Eligible")