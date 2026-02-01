
"""Syntax of the list"""
# _list =[item,item,]

states_of_india = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
# print the item in the list
print(states_of_india[1])
print(states_of_india[0:5])
print(states_of_india[-1])
print(states_of_india[-5:-1])

print("Printing item inside the list using for loop")
for i in states_of_india:
    print(i, end=',')