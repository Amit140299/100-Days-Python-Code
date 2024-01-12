from operator import pos
import random as rd

from sympy import false, true
word_list=['ardvark','baboon','camel']
chosen_word=rd.choice(word_list)

Display=[]
for letter in range(len(chosen_word)):
    Display+="_"
print(Display)

End_of_game=False
while not End_of_game:
    guess=input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        if guess==chosen_word[position]:
            Display[position]=guess
    print(Display)

    if "_" in Display:
        End_of_game=False
    else:
        print("You Win!")