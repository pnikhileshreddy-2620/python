"""
This is code will generate the  password.
It will ask size of the password.
asks for
no of letter
no of symbol
no of number

"""
import  random

alphabeta = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>',
    '/', '?', '|', '\\'
]
print("Welcome to password generate")
user_input = int(input("Tell me the size of the password "))
pss=''
letter_input= int(input("How many letter would  you like to have in your password ?"))
symbol_input= int(input("How many symbol would  you like to have in your password ?"))
number_input= int(input("How many number would  you like to have in your password ?"))
if user_input==letter_input+symbol_input+number_input:
    for letter in range(0,letter_input):
        pss +=random.choice(alphabeta)
    for num in range(0, number_input):
        pss += str(random.choice(number))
    for sys in range(0, symbol_input):
        pss += random.choice(symbol)
else:
    print('check the size')

print('Pattern Identify Your password is :', pss)
shuffle_list=[]
for i in pss:
    shuffle_list.append(i)
random.shuffle(shuffle_list)
hard_pss="".join(shuffle_list)
print("This is hard password ",hard_pss)

