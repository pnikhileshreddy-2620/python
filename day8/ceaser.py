def encode(message,position):
    output=''
    for i in message:
        output +=chr(ord(i)+position)
    return output
def decode(message,position):
    output=''
    for i in message:
        output +=chr(ord(i)-position)
    return output
encode=encode('dell Reddy',2)
decode=decode('fgnn"Tgff{',2)

print(encode)
print(decode)

