import pandas as pd

squirrel = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# # print(squirrel.columns)
# print(squirrel.describe())
# print(squirrel.info)
print(squirrel['Primary Fur Color'].head(50))
output=squirrel['Primary Fur Color'].value_counts()
print(squirrel['Primary Fur Color'].unique())
print(squirrel['Primary Fur Color'].isna().sum())

print(len(squirrel[squirrel['Primary Fur Color']=='Black']))
# pd.DataFrame(output)

output.to_csv('output.csv')