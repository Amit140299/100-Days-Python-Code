# def greet():
#     print("Hello")
#     print("How are you doing?")
#     print("Isn't the weather nice today?")

# def greet_with_name(name):
#     print("Hello")
#     print(f"How are you doing {name}?")
#     print(f"Isn't the weather nice today {name}?")

# def greet_with(name,location):
#     print(f"Hello {name}.")
#     print(f"How is it like in {location}")

# greet_with(location="Mumbai",name="Amit")

def paint_can_calculator(height,width,coverage):
    area=height*width
    no_of_cans=area/coverage
    print(f"You will need {no_of_cans} of paint.")

paint_can_calculator(5,4,5)