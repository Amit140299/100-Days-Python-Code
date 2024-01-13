import random as rd

from Day7_Hangman_words import word_list

from Day7_Hangman_art import stages,logo

print(logo)
chosen_word=rd.choice(word_list)

Display=[]
Lives=6

for letter in range(len(chosen_word)):
    Display+="_"
print(f"{' '.join(Display)}")

End_of_game=False
while not End_of_game and Lives!=0:
    guess=input("Guess a letter:").lower()
    if guess in Display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        if guess==chosen_word[position]:
            Display[position]=guess
    if guess not in chosen_word:
        print(f"You have guessed this {guess} letter that is not in the word. You lose a life.")
        Lives-=1
    print(f"{' '.join(Display)}")
    print(stages[Lives])
    
    if "_" in Display:
        End_of_game=False
    else:
        End_of_game=True
        print("You Win!")
else:
    print("You lose")