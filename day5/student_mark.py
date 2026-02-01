"""
This program generates the 50 random number and add to list.
Using list we are going to perform some basic operation.
using for loop.

"""

import random

student_mark=[]

for i in range(0,50):
    student_mark.append(random.randint(1,100))

print(student_mark)

# Printing the total mark of the student using sum() function
print(sum(student_mark))
# printing the max values in list using max() function
print(max(student_mark))
# printing the max values in list using min() function
print(min(student_mark))
# using for loop adding the total mark
total_mark=0
for i in student_mark:
    total_mark +=i
print(total_mark)

# calculate the 1 to 100

cal =0
for i in range(1,101):
    cal+=i
print(cal)

# testing range function

for i in range(0,10):
    print(i)