""""

Important in Exception
try         : something that might cause exception
except      :do these if there was an exception
else        :do this if there is no exception
finally     :Do this no matter what happens



"""









# with open('text.txt')as f:
#     f.read()
# Above code filenotfounderror exception will come


try:
    with open('text.txt')as f:
        f.read()
except :
    with open('text.txt','w')as f :
        f.write('csdc')
else:
    print("Else")
finally:
    print("Finally")


''''
Error

FileNotFound :file
KeyError :Dict
IndexError :out of range
TypeError : str to num :-'abc'->int Error

'''