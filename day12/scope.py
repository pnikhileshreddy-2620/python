""""Scope"""

global_variable= "GLOBAL"
num=1

def local():
    print(f" Printing the global variable inside the function {global_variable}")
    lo='local'
    print(lo)
    num=2
    print(num)
    print(global_variable)

print(global_variable)
local()
# print(lo) local variable can't used outside of function
print(num)