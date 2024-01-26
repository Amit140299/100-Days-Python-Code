# Calculator

#Add
def add(n1,n2):
    return n1+n2

# Substract
def sub(n1,n2):
    return n1-n2

# Multiply
def multiply(n1,n2):
    return n1*n2

# Division
def division(n1,n2):
    return n1/n2

operations={"+":add,"-":sub,"*":multiply,"/":division}

def Calculator():
    num1=float(input("Whats the first number?"))
    for symbol in operations:
        print(symbol)

    user_choise="y"
    while user_choise=="y":
        num2=float(input("Whats the next number?"))
        operation=input("What operation do you want to perform?")
        answer=operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        user_choise=input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation.").lower()
        if user_choise=="y":
            num1=answer
        elif user_choise=="n":
            Calculator()
        else:
            user_choise=""

Calculator()