import random as rd

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['ardvark','baboon','camel']
chosen_word=rd.choice(word_list)

Display=[]
Lives=6

for letter in range(len(chosen_word)):
    Display+="_"
print(Display)

End_of_game=False
while not End_of_game and Lives!=0:
    guess=input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        if guess==chosen_word[position]:
            Display[position]=guess
    if guess not in chosen_word:
        Lives-=1
    print(Display)
    print(stages[Lives])
    
    if "_" in Display:
        End_of_game=False
    else:
        End_of_game=True
        print("You Win!")
else:
    print("You lose")