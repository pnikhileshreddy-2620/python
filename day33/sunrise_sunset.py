import requests

"""This program about send the data to the external api to get data about sunrise and sunset"""
# Not used ISS  latitude and longitude,But just keep inside code for some purpose
url='https://api.sunrise-sunset.org/json'
iss ='http://api.open-notify.org/iss-now.json'


i_response=requests.get(iss)

latitude =i_response.json()['iss_position']['latitude']
longitude=i_response.json()['iss_position']['longitude']
print(latitude)
print(longitude)

print(i_response)

param={
    "lat":21.7679,
    "lng":78.8718
}

sun = requests.get(url,params=param)
sun.raise_for_status()
data=sun.json()
print(data)


i_response.raise_for_status()