import random
hangmanpic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
randInd = random.randint(0,len(words)-1)
word = words[randInd]
chance = 1
turn = 6
length = len(word)
print("The selected word has", length, 'characters')
alreadyguessed = ''
guess = ''
while(turn>0 and length>0):
    gw = input('Enter a character: ')
    if gw in word:
        if gw in alreadyguessed:
            print('You have already guessed it')
        elif(len(gw)>1):
            print('Enter 1 character at a time or its guessed')
        else:
            length -=1
            print('This word is present')
            alreadyguessed += gw
            guess += gw
            blanks = '_' * len(word)
            for i in range(len(word)):
                if word[i] in gw:
                    blanks = blanks[:i] + word[i] + blanks[i+1:]
            for letter in blanks:
                print(letter, end='')
            print()
    elif guess == word:
        print('You got it')
        print(word)
        break
    else:
        print('The character is not present!')
        print(hangmanpic[chance])
        chance += 1
        turn -= 1
        length +=1
    print(alreadyguessed)
    if chance == 7:
        print('You could not guess  it.')
        print('The word selected was:',word)
