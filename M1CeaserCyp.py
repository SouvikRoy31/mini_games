alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = input('Please enter Message:')

key = int(input('Enter any key between 1-26: ' ))
newMsg = ''

for character in msg:
    if character.islower():
        if character in alphabet:
            pos = alphabet.find(character)
            newpos = (pos+key)%26
            newChar = alphabet[newpos]
            newMsg += newChar
    elif character.isupper():
        if character in alphabetup:
            pos = alphabetup.find(character)
            newpos = (pos+key)%26
            newChar = alphabetup[newpos]
            newMsg += newChar
    else:
        newMsg += character

print('The encrypted message is:',newMsg)
