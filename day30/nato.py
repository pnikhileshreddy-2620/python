import pandas as pd

data =pd.read_csv('C:/Users/pongredd/OneDrive - Capgemini/Desktop/Python/python/day26/nanto.csv')

# Topic covered there is  list/dict comprehensive
nato_dict ={row.Letter:row.Code for (index,row) in data.iterrows()}




user = input("Enter the word").upper()
i=0
while i>=0:

    try:
        Full_word =[ nato_dict[i] for  i in user]
        i +=1
        print(Full_word)
        break
    except KeyError:
        print("Sorry, Only letter in the alphabet please ")
        user = input("Enter the word").upper()

