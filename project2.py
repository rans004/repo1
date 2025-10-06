import random

print('welcome to the RPS game')
emojis=dict(rock="🪨",paper="📃",scissors="✂️")
game=["rock","paper","scissors"]
random_number=random.choice(game)
random_number1=emojis[random_number]
while True:
 try:
  user_choice=input("whats your take\n")
  user_choice1=emojis[user_choice]
  print(user_choice1)
 except NameError:
   print("enter a valid choice")
 if user_choice1==random_number1:
    print("congrats")
    break
 elif user_choice not in game:
   print("wrong input")

 else:
    print("you lost,do you want to play again?")
    second_chance=input()
    if second_chance=="yes":
      continue
    else:
      print("thanks for your time")
      break