status = True
count = 1
import random
ri=random.randint(1,6)
while(status==True):
    gn=input("Enter any dice number '1-6': ")
    if(int(gn)==int(ri)):
        print("Your guess is Correct!")
        print("You took " + str(count) + " gusses." )
        p=100-(count/6)*100
        print("Your probablity guess is: " + str(p))
        status = False
    else:
        print("Your guess is Wrong")
        status = True
        count = count+1
