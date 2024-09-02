import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"snake" : 1, "water" : -1, "gun" : 0}
reversedict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youdict[youstr]

print(f"You chose{reversedict[you]}/n Computer chose {reversedict[computer]}")

if(computer == you):
    print("its Draw!")

elif(computer == -1 and you == 1):
    print("You Win!")

elif(computer == -1 and you ==0):
    print("You Lose! ): ")

elif(computer == 1 and you == -1):
    print("You Lose! ): ")

elif(computer == 1 and you ==0):
    print("You Win! ")

elif(computer == 0 and you ==-1):
    print("You Win! ")

elif(computer == 1 and you ==0):
    print("You Lose! ): ")


