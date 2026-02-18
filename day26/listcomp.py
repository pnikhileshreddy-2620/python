import  pandas as pd
data = pd.read_csv('nanto.csv')
my_input = input("Enter the word ").upper()
phot ={v['Letter']:v['Code']for i,v in data.iterrows()}
final_op =[ phot[i] for i in my_input if i in phot]
print(final_op)
