import random

squ ={i:i*i for i in range(0,11)}
print(squ)

names = ["Al", "John", "Maria", "Alexander", "Christopher"]

number =[1,2,3,4,5]

dic_name_number={k:i for i,k in zip(names,number)}
print(dic_name_number)

dic_name_number={i:random.randint(1,100) for i in names}
print(dic_name_number)

passed ={k:v for k,v in dic_name_number.items() if v>=60 }
print(passed)

passed ={k:"Passed" for k,v in dic_name_number.items() if v>=60 }
print(passed)

