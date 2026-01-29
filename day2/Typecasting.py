"""
❌ Errors in Type Casting (Python) — RULES

1️⃣ TypeError occurs
→ when conversion between two data types is not possible

2️⃣ ValueError occurs
→ when data type is correct but value is invalid

3️⃣ OverflowError occurs
→ when value is too large to convert


Type Casting (Python) — RULES

1️⃣ Type casting means converting one data type into another

2️⃣ Python supports two types of type casting
→ Implicit type casting
→ Explicit type casting

3️⃣ Implicit type casting is done automatically by Python

4️⃣ Explicit type casting is done using functions
→ int(), float(), str(), list(), tuple(), set()

5️⃣ Lower data types are converted to higher data types automatically
→ int → float → complex

6️⃣ Complex numbers cannot be converted to int or float

7️⃣ String can be converted to number only if it contains numeric value

8️⃣ Float to int conversion removes decimal part

9️⃣ Set type casting removes duplicate values

🔟 Invalid type casting causes errors



"""


value ='123'
print(type(value))
print(type(int(value)))

print("Number Of letter in your name  :"+ str(len(input("Enter the name "))))