import requests
from xlrd.timemachine import fprintf

key='1ef386568e25f63ed9bc614463cf8ddc'
day5='https://api.openweathermap.org/data/2.5/forecast'
url='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

param ={
    "lat":20.593683,
    "lon":78.962883,
    "appid":key,
    "cnt":3

}

id=[]

response = requests.get(day5,params=param)
response.raise_for_status()
print(response.status_code)
print(response.raise_for_status())
response_json=response.json()
# print(response_json)
# print(response_json['list'][0]['weather'][0]['description'])
print(type(response_json))
print(response_json['list'])
print("--------------------------")
print(response_json['list'][0])

print("--------------------------")
print(response_json['list'][0]['weather'][0])
print("_"*20)
print(response_json['list'][0]['weather'][0]['id'])

print("--------------------------")
print(response_json['list'][0]['weather'][0]['description'])

print("*"*20)
print(response_json)

# for i in enumerate(response_json,start=1):
#     print(response_json['list'][int(i[0])]['weather'][0]['description'])


for i in range(len(response_json['list'])):
    id.append(response_json['list'][i]['weather'][0]['id'])


def notify(list):
    for item in list:
        if item<700:
            return "Bring Umbrella"
        else:
            return "Not Need bring Umbrella"
print(notify(id))
