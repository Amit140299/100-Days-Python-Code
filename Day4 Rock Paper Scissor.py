# import random

# random_integer=random.randint(1,6)
# random_float=random.uniform(0,5)

# print(random_integer)
# print(random_float)

# random_side=random.randint(0,1)
# print(random_side)

# List

# states_of_India=["Maharashtra","Tamil nadu","Karnataka","Gujarat","Odisha","Rajasthan","Uttar Pradesh","Madhya Pradesh","Chattisgarh"]
# # print n^th item from the list
# print(states_of_India)
# print(states_of_India[1])

# states_of_India[1]="Tamil Nadu"

# states_of_India.append("Kerla")
# print(states_of_India)

# states_of_India.extend(["Delhi",'West Bengal'])
# print(states_of_India)

# len(states_of_India)


# # Who will pay the bill
# import random

# names=["Amit","Bobby","Chinmay","Klabi","Utkarsha"]
# length=len(names)
# print(length)
# random_name_index=random.randint(0,length-1)
# random_name=names[random_name_index]
# print(f"{random_name} will pay the bill")


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

# list1=[" "," "," "]
# list2=[" "," "," "]
# list3=[" "," "," "] 
# gap=[list1, list2,list3]
# print("Hiding your treasure! x marks the spot.")
# position=input()
# letter=position[0].lower()
# abc=["a","b","c"]
# letter_index=abc.index(letter)
# print(letter_index)
# number_index=int(position[1])-1
# gap[letter_index][number_index]="X"
# print(f"{list1}\n,{list2}\n,{list3}")


# Final Project Rock Paper Sissor

import random
import sys

Rock='''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper='''
     _______
---'    ____)____
           ______)
          _______
         _______)
---.__________)
'''
Scissors='''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor")
user_input=int(input())
if user_input==0:
    print(Rock)
elif user_input==1:
    print(Paper)
elif user_input==2:
    print(Scissors)
else:
    print("Invalid input please try again")
    sys.exit()

Computer_input=random.randint(0,2)  
print("Computer Chose:")
if Computer_input==0:
    print(Rock)
elif Computer_input==1:
    print(Paper)
else:
    print(Scissors)

if user_input==0:
    if Computer_input==0:
        print("It's a tie")
    elif Computer_input==1:
        print("You lose")
    else:
        print("You Win!")
        
elif user_input==1:
    if Computer_input==0:
        print("You Win!")
    elif Computer_input==1:
        print("It's a tie")
    else:
        print("You lose")

elif user_input==2:
    if Computer_input==0:
        print("You lose")
    elif Computer_input==1:
        print("You Win!")
    else:
        print("It's a tie")