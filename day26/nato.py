nato_phonetic = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "London",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}
user_input = input("Enter the name :").upper()

# name=[]
nato_alpha=[]
# for i in user_input:
#     name.append(i)
# print(name)
# for k,v in nato_phonetic.items():
#     for letters in name:
#         if letters in k:
#             nato_alpha.append(v)
# print(nato_alpha)

for letter in user_input:
    print(letter)

for letter in user_input:
    if letter in nato_phonetic:
        nato_alpha.append(nato_phonetic[letter])
print(nato_alpha)