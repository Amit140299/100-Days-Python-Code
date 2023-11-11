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
import random

names=["Amit","Bobby","Chinmay","Klabi","Utkarsha"]
length=len(names)
print(length)
random_name_index=random.randint(0,length-1)
random_name=names[random_name_index]
print(f"{random_name} will pay the bill")


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

list1=[" "," "," "]
list2=[" "," "," "]
list3=[" "," "," "]
print("Hiding your treasure! x marks the spot.")
position=input()
