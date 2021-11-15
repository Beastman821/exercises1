
word = list(input("what's your word? "))

if word > [2]:
    if word[-3:] == 'ing':
        word += 'ly'
    else:
        word += 'ing'