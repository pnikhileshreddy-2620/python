

def greet():
    print("Hello welcome to python programming")
greet()

# FUNCTION WITH
# DEFINE THE FUNCTION
def my_funcrtion(something):
    print(something)

# CALLING FUNCTION
my_funcrtion('name')

def greet_with_name(parameter):
    print(parameter)
greet_with_name('argument')

# POSITIONAL ARGUMENT VS KEYWORD ARGUMENT

# Keyword Argument
def greet_with(name,location):
    print(f'My name is {name} and my location {location}')

greet_with('nikki','AP')
greet_with(location='TS',name='nikki')

# default value
# position argument
def greet_with(name,location='HYD'):
    print(f'My name is {name} and my location {location}')

greet_with('nikki','AP')
greet_with(location='TS',name='nikki')
greet_with(name='dell')