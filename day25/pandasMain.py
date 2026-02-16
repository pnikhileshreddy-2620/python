import pandas as pd

data_file=pd.read_csv('weather_data.csv')
print(data_file)
print(data_file['temp'])
print(data_file['day'],data_file['condition'])

# convert .csv file into different

data_dict =data_file.to_dict()
print(data_dict)

data_html =data_file.to_html()
print(data_html)
print("000000000000")
temp_list = data_file['temp'].to_list()
print(temp_list)

print(sum(temp_list))
print(sum(temp_list)/len(temp_list))

# pandas
print(data_file['temp'].mean())

print(data_file['temp'].max())
print(data_file['temp'].min())

print(data_file['day'])
print(data_file['condition'])
print(data_file['condition'].unique())
print(data_file.temp)
print(data_file[0:2])

print(data_file[data_file.day=='Monday'])

print(data_file[data_file.temp==max(data_file.temp)])
print("convert celsius into fahrenheit")
print((data_file.temp*9/5)+32)


name =['dell','pc']
df=pd.DataFrame(name)
print(type(df))

dict_frame={

    "name":['dell','hp','lenova','Pc'],
    "price":[1000,2000,900,500]

}

convert_new_data= pd.DataFrame(dict_frame)
convert_new_data.to_csv("New_price.csv")