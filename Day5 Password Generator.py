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

student_scores=input().split()
index=0
hightest_score=0
for score in student_scores:
    if int(score)>hightest_score:
        hightest_score=int(score)
        
print(hightest_score)