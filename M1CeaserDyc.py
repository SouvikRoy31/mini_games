alphabet = 'abcdefghijklmnopqrstuvwxyz'
msg = input('Please enter encrypted Message: ')
key = int(input('Enter the key: ' ))
newMsg = ''

for character in msg:
    if character in alphabet:
        pos = alphabet.find(character)
        newpos = (pos-key)%26
        newChar = alphabet[newpos]
        newMsg += newChar
    else:
        newMsg += character

print('The decrypted message is:',newMsg)
