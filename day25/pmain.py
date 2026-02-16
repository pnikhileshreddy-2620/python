
""""Here is the 3 ways doing same thing """

# with open('weather_data.csv','r')as f:
#     pan = f.readlines()
#     print(pan)
# with open('weather_data.csv','r')as f:
#     pan = f.read()
#     print(pan)


# import  csv
#
# # temperature=[]
# with open('weather_data.csv','r')as data_file:
#     data =csv.reader(data_file)
#     temperature = []
#     for rows in data:
#         if rows[1]!='temp':
#             temperature.append(int(rows[1]))
#     print(temperature)


import pandas as pd

data_file=pd.read_csv('weather_data.csv')
print(data_file)
