# Dctionary is associated with a key and a value related to a key
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again."}

programming_dictionary["Bug"]

# you can add a key and a value in a dictionary by simply writing below code
programming_dictionary["Loop"]="Action of doing something ovr and over again"
print(programming_dictionary)

# You can create an empty dcitionary and also wipe the existing dictionary by below method
# empy_dictionary={}
# print(empy_dictionary)
# programming_dictionary={}
# print(programming_dictionary)

# Edit a key's value in a dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary)

#  Loop throa a dictionary
for key in programming_dictionary:
    print(key,programming_dictionary[key])