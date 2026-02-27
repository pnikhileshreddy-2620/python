import string
"""
Type hints (or type annotations) are a special syntax in Python (introduced in PEP 484 with Python 3.5) that allow you to indicate the expected data types of variables, function arguments, and return values. They are primarily used by third-party tools (like static type checkers and IDEs) to help developers catch type-related bugs early, improve code readability, and enhance editor support like code completion, without affecting the program's runtime behavior. 
"""
age :int
name :str
gender :str

#  -> used to except output of the function
def voter_check(age:int)->bool:
    if age >= 18:
        return True
    else:
        return False

print(voter_check(10))
print(voter_check(20))

if voter_check(10):
    print("Your Eligible")
else:
    print("Not Eligible")