# write a python program that counts the number of characters in a string
# collections is a built in python module that implements specialized container datatypes 
# And Counter is a subclass of dict that specially designed for counting hashable objects
from collections import Counter

words = input('type your word in... ')

print(Counter(words))

