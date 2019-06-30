import random
gn=input("Enter your guess: ")
e=random.randint(1,6)
if(int(e)==int(gn)):
    print("You guessed Correct")
else:
    print("Your guess is Wrong")
    print ('Your Guess:'+str(gn))
    print ('Dice Number:'+str(e))
