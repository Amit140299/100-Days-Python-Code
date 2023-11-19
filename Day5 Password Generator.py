# fruits=["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+"Pie")

# print(("172 1271 223 121 454").split())
# studnet_heights=input().split()
# n=0
# Total_height=0
# for height in studnet_heights:
#     print(height)
#     Total_height+=int(height)
#     n+=1
# Avg_height=Total_height/n
# print(f"Total Heigth= {Total_height}")
# print(f"Total Students= {n}")
# print(f"Avgerage Height= {Avg_height}")


# Maximum from the list and finding index
# student_scores=input().split()
# index=0
# hightest_score=0
# n=0
# for score in student_scores:
#     if int(score)>hightest_score:
#         hightest_score=int(score)
#         index=n
#     n+=1
# print(hightest_score)
# print(index)

# for number in range(1,10):
#     print(number)

# Sum of all he numbers between 1 to 100
# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# Sum of all the even numbers between user defined numbers
# total=0
# starting_number=int(input())
# if starting_number%2==0:
#     for number in range(starting_number,101,2):
#         total+=number
# print(total)


# FizzBuzz Game

# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)
# Final Project Password Generator


# list1=["a",'b','c']
# list2=['s','g','t',]

# list3=list1+list2
# print(list3)

import random as rd

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols=['!','@','#','$','%','^','&','*','(',')','-','_','+']

print("Welcome to the PyPassword Generator!")
Pass_level=input("What level of password do you want to generate? Type 'Easy or 'Hard' \n").lower()

nr_letters=int(input("How many letters would you like to have in your password?\n"))
nr_numbers=int(input("How many numbers would you like to have in your password?\n"))
nr_symbols=int(input("How many symbols would you like to have in your password?\n"))

password=""

if Pass_level=='easy':
    for i in range(0,nr_letters):
        password+=rd.choice(letters)

    for i in range(0,nr_symbols):
        password+=rd.choice(symbols)

    for i in range(0,nr_numbers):
        password+=rd.choice(numbers)

    print(password)

elif Pass_level=="hard":
    total_length=nr_letters+nr_numbers+nr_symbols
    combined_list=letters+symbols+numbers

    for i in range(0,total_length):
        password+=rd.choice(combined_list)

    print(password)
else:
    print("Choose a valid option.")