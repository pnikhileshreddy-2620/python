import  pandas as pd

data = pd.read_csv('nanto.csv')
print(data)


new_dict= {row['Letter']:row['Code'] for (index,row) in data.iterrows()}

print(new_dict)

output=[]

user =input("Enter word ").upper()

for letters in user:
    if letters in new_dict:
        output.append(new_dict[letters])
print(output)