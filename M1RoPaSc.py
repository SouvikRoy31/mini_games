"""
User se input lena h
rock paper or scissor
computer se random generate krwana h(1,3)
1-rock, 2-paper, 3-scissor

"""
def fig(x):
    if x == 1:
        print('O')
    elif x == 2:
        print('____')
    elif x == 3:
        print('8<')
import random
print("What do you want to choose?")
user = input("Rock (r), Paper (p), Scissor (s): ")
comp = random.randint(1,3)
if (user == 'r'): #and comp == 1:
    choice = 1
if (user == 'p'): #and comp == 2:
    choice = 2
if (user == 's'): #and comp == 3:
    choice = 3
if(choice == comp):
    print("you Choose")
    fig(choice)
    print("Computer choose " )
    fig(comp)
    print("Its a DRAW!")
elif choice == 1 and comp == 3:
    print("you Choose")
    fig(choice)
    print("Computer choose " )
    fig(comp)
    print("You Won")
elif choice == 1 and comp == 2:
    print("you Choose")
    fig(choice)
    print("Computer choose " )
    fig(comp)
    print ("Computer Won")
elif choice == 2 and comp == 1:
    print("you Choose")
    fig(choice)
    print("Computer choose ")
    fig(comp)
    print("You Won")
elif choice == 2 and comp == 3:
    print("you Choose")
    fig(choice)
    print("Computer choose ")
    fig(comp)
    print("Computer Won")
elif choice == 3 and comp == 1:
    print("you Choose")
    fig(choice)
    print("Computer choose ")
    fig(comp)
    print("You Won!")
elif choice == 3 and comp == 2:
    print("you Choose")
    fig(choice)
    print("Computer choose ")
    fig(comp)
    print("Computer Won")
