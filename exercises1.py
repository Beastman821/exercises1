# Write a python program to calculate the length of a string
# The len function is key here which tells the program how many characters are in a string

# 1st solution
word = len(input("type a word or phrase... "))

print(f"the length of the string is: {word}")

# 2nd solution
# the string_length is the varable then str1 is the string being counted
def string_length(str1):
    # count is the varable counting the word so it has to start a zero
    count = 0
    # the for loop for characters in str1 count every character then add one
    for char in str1:
        count += 1
    return count
    # after the for loop counts the characters it returns untill it hits zeros
print(string_length('word'))