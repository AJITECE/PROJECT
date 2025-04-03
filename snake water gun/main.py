'''
game project from harry 

-1 : paper
1 : rock
0 : scissor

'''
import random
computer=random.choice([1,-1,0])
user=input("Enter your number: ")
userDic={"r":1,
         "p":-1,
         "s":0 }
userReverseDic={ 1:"rock",
                -1:"paper",
                0:"scissor"}

if user not in userDic:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
else:
    userInput = userDic[user]

print(f"you choose: {userReverseDic[userInput]}\ncomputer choose : {userReverseDic[computer]}")

if(computer == userInput):
      print("Game draw")
else:
   
    if(computer==-1 and userInput==0):
           print("You win! ")
    elif(computer==-1 and userInput==1):
           print("You lose!")
    elif(computer==1 and userInput==-1):
           print("You lose!")
    elif(computer==1 and userInput==0):
           print("You lose") 
    elif(computer==0 and userInput==-1):
           print("You lose!")
    elif(computer==0 and userInput==1):
           print("You Won!")

    else:
           print("something went wrong")

###another smethod to write in shortcut

# else:
#         # Winning conditions for the user
#         if (computer == -1 and userInput == 0) or \
#            (computer == 1 and userInput == -1) or \
#            (computer == 0 and userInput == 1):
#             print(" You lose! ")
#         else:
#             print(" You won!")  