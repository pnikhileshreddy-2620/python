# function with argument
def add(a,b,c):
    print(a+b+c)
#     calling function with keyword parameter
add(c=1,a=3,b=2)

# function with keyword argument

def adds(a=1,b=1,c=1):
    print(a+b+c)
    print(a,b,c)

# calling the function and changing the value in parameter
# something no parameter is there, default value will be added to function call
adds(3,4,)
adds(1)