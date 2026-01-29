# Taking input form the user using input() function
"""
input() is a built-in Python function used to take input (data) from the user.
Whatever the user types becomes a string.

INPUT() FUNCTION RULES (PYTHON)

input() is used to take data from the user.

input() always returns a string.

Program waits until the user presses Enter.

Text inside input(" ") is a prompt message.

Store input in a variable.

name = input("Enter name: ")


Numbers entered using input() are treated as text.

x = input("Enter number: ")


Convert input to integer using int().

age = int(input("Enter age: "))


Convert input to float using float().

price = float(input("Enter price: "))


Without conversion, math operations will be wrong.

"10" + "20" = "1020"


You can take multiple inputs.

a = input("Enter a: ")
b = input("Enter b: ")


input() can be used inside expressions.

total = int(input()) + int(input())


Use strip() to remove extra spaces.

name = input().strip()


String methods can be used with input().

name = input().upper()


Wrong input type causes error during conversion.

int("abc")  # error


Always validate input in real programs.

input() is used in interactive programs only.

input() works with if, loops, and functions.

REMEMBER:

input() → string

"""
from pandas.util import capitalize_first_letter

name = input("what is your name: ")
print('HI '+capitalize_first_letter(name)+' Welcome')
print('Hi ' +name.capitalize()+ ' welcome ')

print('Hi ' + input("Enter the name inside the function "))
