status = True
import random
ri = random.randint(0,9999)
count = 1
while(status==True):
    gn = int(input("Enter any (whole)number between '0-9999': "))
    if(ri==gn):
        print("Your guess is Correct")
        print("You took " + str(count) + " gusses." )
        status = False
    elif(gn>ri):
        print("Your guessed number is Greater than the Random Number")
        status = True
        count = count+1
    elif(ri>gn):
        print("Your gussed number is Less than the Random Number")
        status = True
        count = count+1
    else:
        print("Enter a Valid number!")
        count = count+1
