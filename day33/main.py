from logging import raiseExceptions

import requests

url ='http://api.open-notify.org/iss-now.json'

response=requests.get(url)
# if response.status_code==200:
#     raise Exception("Login")
# elif response.status_code ==400:
#     raise Exception("Bad Request")
# elif response.status_code==500:
#     raise Exception('Internal Server Error')
# elif response.status_code==404:
#     raise Exception('Page Not Found')
# elif response.status_code==500:
#     raise Exception('Internal Server Error')
# elif response.status_code==502:
#     raise Exception('Bad Gateway')
# {'timestamp': 1772081450, 'message': 'success', 'iss_position': {'longitude': '162.7794', 'latitude': '-51.3658'}}
iss=[]
print(response.raise_for_status())

print(response.json())

print(response.json()['iss_position'])
print(response.json()['iss_position']['longitude'])
print(response.json()['iss_position']['latitude'])

longitude=response.json()['iss_position']['longitude']
latitude=response.json()['iss_position']['latitude']
full_data=response.json()['iss_position']

iss.append(response.json())

tup =(latitude,longitude)

