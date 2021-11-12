# it's a program to get a string from a given string where all occurrences of its first char have been changed to $ except the first char itself
a = input("type your word... ")
# in the def specialreplace the variable firstchar is set to the first character 
# then the modifierchar is set to the next character saying to replace any letter like the firstchar to a $
def specialreplace(s):
    firstchar = s[0]
    modifierchar = s[1:].replace(firstchar, "$")
    print(firstchar + modifierchar)

specialreplace(a)

# This was my first attempt at the challenge
#print(a.replace("r", "$", ))

