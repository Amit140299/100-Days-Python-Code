# Leap year check

# # Which year you want to check?
# year=int(input())
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("it is a leap year")
# else:
#     print('It is not a leap year')


# Rollercoster bill generator
# print("Wlcome to rollercoster!")
# height=int(input("what is your height in cm? "))
# bill=0
# if height>=120:
#     print("You can ride the rollercoster!")
#     age=int(input("What is your age?"))
#     if age<=12:
#         print("Child tickets are ₹. 399.")
#         bill=399
#     elif age<=18:
#         print("Youth tickets are ₹. 599.")
#         bill=599
#     else: 
#         print("Adult ticket are ₹ 999.")
#         bill=999
#     wants_photo=input("Do you want a photo taken? Y or N.")
#     if wants_photo=="Y" or wants_photo=="y":
#         # bill=bill+250
#         bill+=250
#         print(f"Your total bill is ₹{bill}")
#     elif wants_photo=="N" or wants_photo=="n":
#         print(f"Your total bill is ₹{bill}")
#     else:
#         print("Please give a valid input")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    

# Pizza bill generator

# print("Thank you for choosing Python Pizza Deliveries!")
# size=input("What size of pizza do you want? S, M or L ")
# add_pepperoni=input("Do you want pepperoni? Y or N ")
# extra_cheese=input("Do you want extra cheese? Y or N ")
# bill=0

# if size=="S" or size=="s":
#     bill+=150
# elif size=="M" or size=="m":
#     bill+=200
# elif size=="L" or size=="l":
#     bill+=250
# else:
#     print("Please enter a valid size.")

# if bill>0:
#     if add_pepperoni=="Y" or add_pepperoni=="y":
#         if size=="S" or size=="s":
#             bill+=20
#         else:
#             bill+=30
#     if extra_cheese=="Y" or extra_cheese=="y":
#         bill+=1
# print(f"Your final bill is ₹{bill}")

# print("The love calculator is calculating you score...")
# name1=input("What is your name? ")
# name2=input("What is their name? ")

# combined_Names=name1+name2
# # Convet it in lover case
# lower_names=combined_Names.lower()
# t=lower_names.count("t")
# r=lower_names.count("r")
# u=lower_names.count("u")
# e=lower_names.count("e")
# first_digit=t+r+u+e

# l=lower_names.count("l")
# o=lower_names.count("o")
# v=lower_names.count("v")
# e=lower_names.count("e")
# second_digit=l+o+v+e

# score=int(str(first_digit)+str(second_digit))
# if score<10 or score>90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score>40 and score<50:
#     print(f"Your score is {score}, you are alrigth together.")
# else:
#     print(f"Your score is {score}")


# Treasure Island

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

Welcome to Treasure Island!
Your mission is to find treasure.''')

choice1=input(print('You\'re a crossroad where do you want to go? Type "left" or "right".')).lower()
# if choice1=='left':
#     choice2=input('''You've come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.''').lower()
#     if choice2=="wait":
#         choice3=input('''You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color 
# do you choose''').lower()
#         if choice3=="red":
#             print("it's a room full of fire. Game Over.")
#         elif choice3=="yellow":
#             print("You fond the treasure. You Win!")
#         elif choice3=="blue":
#             print("You entered a room of beasts. Game Over.")
#         else:
#             print("You chose the door that doesn't exist. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over")
# else:
#     print("You fell into a hole, Game Over.")