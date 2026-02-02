import string

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
data = input("Please type the data: ")
position = int(input("Enter the number of positions to shift: "))

def encrypt(data, position):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    final_value = []

    for ch in data:
        if ch in lower:
            idx = lower.index(ch)
            new_idx = (idx + position) % 26
            final_value.append(lower[new_idx])
        elif ch in upper:
            idx = upper.index(ch)
            new_idx = (idx + position) % 26
            final_value.append(upper[new_idx])
        else:
            final_value.append(ch)  # Keep non-alphabet characters unchanged

    return ''.join(final_value)

def decrypt(data, position):
       return encrypt(data, -position)

if direction == 'encode':
    result = encrypt(data, position)
    print(result)
elif direction == 'decode':
    result = decrypt(data, position)
    print(result)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")