# Guess-game 
import random
n=random.randint(0,1000)
a=-1
guess=0

while(a!=n):
    guess=guess+1
    a=int(input("Guess the number:"))
    if(a<0 or a>1000):
        print("enter the guessing number between 0 to 100")
    
    if(a>n):
        print("enter the lower number")
    elif(a<n):
        print("enter the higher number")

print(f"you guess the correct number {n} in {guess} attempt")