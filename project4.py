text=open("demofile.txt")
text1=text.read()
text2=text1.split()
wc=len(text2)
print(f"your word count is {wc}")

main_text=input('enter your text\n')
new_text=main_text.split()
word_count=len(new_text)
print(f"your word count is {word_count}")

import random

print("welcome to the guessing game")

sports=["football","basketball","tennis","hockey","rugby","golf","cricket"]
fruits=["pear","grapes","orange","banana","mango"]
animals=["lion","camel","dog","cat","goat"]

words=sports +fruits+animals
random_word=random.choice(words)
if random_word in animals:
    print("hint:\'it's\' an animal")
elif random_word in fruits:
    print("hint:its a fruit")
else:
    print("hint:its a sport")
    user_guesses=" "
    chances=5
    while chances>0:
        wrong_guess=0
        for x in random_word:
            if x in user_guesses:
                print("x",end=" ")
            else:
                wrong_guess+=1
                print("_",end=" ")
        if wrong_guess==0:
            print("\n congrats you have won the game and the anser is",random_word)
            break
        guess= input("make your guess\n")
        user_guesses+=guess
        if x not in random_word:
            chances-=1
            print("you made the wrong guess ,try again")
            if chances==0:
                print("you have exhausted your chances,game over,the word is",random_word)


