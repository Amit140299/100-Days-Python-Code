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
starting_number=int(input())
ending_numbers=int(input())
if starting_number%==0:
total=0
for number in range(starting_number,101,2):
    total+=number
print(total)