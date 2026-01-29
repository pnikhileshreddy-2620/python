""" A variable in Python is just a name that stores a value in memory.
Think of it like a labeled box—you put something in the box,
 and you can use it later by calling the label.
 Rules for variable names

✅ Must start with a letter or _
✅ Can contain letters, numbers, _
❌ Cannot start with a number
❌ Cannot use Python keywords (if, for, while, etc.)

valid
my_name
_age
total2

invalid
my_name
_age
total2

"""

# my_name is variable
my_name = input('What is your name :')
print("My name is "+my_name)