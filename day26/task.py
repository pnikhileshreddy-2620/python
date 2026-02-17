sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_string= [i for i in sentence.split()]
print(word_string)
result ={ i:len(i) for i in word_string}
print(result)