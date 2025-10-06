import random

print("welcome to the guessing game")
random_number=random.randrange(1,100)
while True:
  try:
    user_number1=int(input("guess the preferred number \n"))
  except ValueError:
    print("enter a valid number")
  if random_number==user_number1:
    print("congrats")
    break
  elif random_number>user_number1:
    print("too low")
  else:
    print('too high')