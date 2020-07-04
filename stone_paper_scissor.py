from random import randint
t=["stone","paper","scissor"]
computer=t[randint(0,2)]
player=False
while player==False:
#set player to true    
    player=input("stone,paper,scissor? \n")
    if player==computer:
        print("Tie")
    elif player=="stone":
        if computer=="paper":
            print("You lose!!",computer,"covers",player)
        else:
            print("You win!!",player,"smashes",computer)
    elif player=="paper":
        if computer=="scissor":
            print("You lose!!",computer,"cut",player)
        else:
            print("You win!!",player,"covers",computer)
    elif player=="scissor":
         if computer=="stone":
             print("You lose!!",computer,"smash",player)
         else:
             print("You win!!",player,"cut",computer)
    else:
        print("OOPS!! Invalid check the spelling")
    
    #set player to false to continue the loop    
    player=False
    computer=t[randint(0,2)]
