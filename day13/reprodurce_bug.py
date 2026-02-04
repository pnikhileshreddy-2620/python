import  random

dice =[1,2,3,4,5,6]
# num =  random.randint(1,6) This line of code produce the bug.
'''This line will work fine without any bug'''
num= random.randint(0,5)
print(dice[num])