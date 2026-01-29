"""

📌 Important Rules / Notes

Counts characters in a string (spaces included)

Counts elements, not values

For dictionaries, counts keys

Cannot be used on numbers (int, float)

len(10)   # ❌ TypeError


"""

print(len("dell"))
print(len(str(1)))
# TypeError: object of type 'int' has no len()
# print(len(1)) :-error


# How to check the data type use type() function

print(type("Dell"))
print(type(1))
print(type(2.0))
print(type(True))