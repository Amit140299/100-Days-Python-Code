# def add_sum(a,b):
#     result=a+b
#     # print(result)
#     return result
# a=0
# for i in range(1,4):
#     a=add_sum(i,a)

# print(a)

# def format_name(f_name,l_name):
#     """Take first and last name of user and return it in proper name formatting."""
#     if f_name=="" or l_name=="":
#         return "You did't provide valid inputs."
#     first_name=f_name.title()
#     last_name=l_name.title()
#     return f"{first_name} {last_name}"

# print(format_name(input("What is your first name?"),input("What is your last name?")))

def days_in_month(y=int(input("Enter a year. ")),m=int(input("Enter a month. "))):
    """takes input from user for any year and month and shows number of days in that month."""
    number_of_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%4==0:
        if y%100==0:
            if y%400==0:
                if m==2:
                    return  number_of_days[m-1]+1
                else:
                    return number_of_days[m-1]
            else:
                return number_of_days[m-1]
        elif m==2:
            return number_of_days[m-1]+1
        else:
            return number_of_days[m-1]
    else:
        return number_of_days[m-1]

print(days_in_month())