# One way of doing
number =[1,2,3]
new_number =[]
for i in number:
    new_number.append(i+1)
print(new_number)

# This another way of doing
new_number_compre=[i+1 for i in number]
print(new_number_compre)

# Square the first 10 number

square=[i**2 for i in range(1,11)]
print(square)

name ='dell'
name_list = [ i for  i in name]
print(name_list)

double_number =[ i*2 for i in range(2,6)]
print(double_number)


names = ["Al", "John", "Maria", "Alexander", "Christopher"]

short_name =[  i for i in names if len(i)<=4]
print(short_name)

upper_case_name = [  i.upper() for i in names if len(i)>5]
print(upper_case_name)