import random

print("welcome to the dice rolling game")
while True:
 choice=input("choose yes or no to play\n")
 if choice=="yes":
    print(random.randrange(1,6))
 elif choice=="no":
    print("buh why")
    break
 else:
    print("wrong input,try again")

