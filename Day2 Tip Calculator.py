# 1.Create a greeting for your program.
print('Wlcome to Tip Calculator!')
# 2.Ask the user for the total bill.
Total_Bill=float(input("What was the total bill?\n"))
# 3.Ask the user for number of people to split the bill.
People=float(input('How many people to split the bill?\n'))
# 4.Ask the user for percentage tip they would like to give.
Tip_perecent=float(input('What percentage tip would you like to give? 10,12or 15\n'))
# 5. Calculate final bill per person.
Final_bill=(Total_Bill+((Total_Bill*Tip_perecent)/100))/People
# 6. Show them the amount per person.
print(f'Each person should pay:{round(Final_bill,2)}')
# 7.Make sure the input curesor shows on new line