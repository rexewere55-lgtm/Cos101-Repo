#weekly expenses calculator
student_name= input("Student name: ")
daily_transport_cost= float(input("Daily transport cost:"))
daily_feeding_cost= int(input("Daily feeding cost: "))
days_on_campus= int(input("Number of days on campus: "))
Other_weekly_expenses= float(input("Other weekly expenses:"))

#Calculations
transport_total = daily_transport_cost * days_on_campus
feeding_total = daily_feeding_cost * days_on_campus
weekly_total = transport_total + feeding_total + Other_weekly_expenses

#weekly expenses summary                                   
print("Weekly student expenses")
print("Student:", student_name )
print(f"transport total: NGN {transport_total:.2f}")
print(f"feeding total:NGN {feeding_total:.2f}")
print(f"Other weekly expenses: NGN {Other_weekly_expenses:.2f}")
print(f"weekly_total: NGN {weekly_total:.2f}")

#Weekly budget
days = int(input("Enter the number of days:"))
if days < 0:
    print("Invalid input! Number of days cannot be negative.")
else: total_expenses = 0
for day in  range(1, days + 1):
      expense = int(input(f"Enter expense for day {day}: "))

      if expense < 0:
          print("Invalid input! Expense cannot be negative.")
break
total_expenses += expense

   
print("Total expenses:", total_expenses)

budget = int(input("Enter your weekly budget: "))

if budget < 0:
              print("Invalid input! Budget cannot be negative.")

elif total_expenses < budget: remaining = budget - total_expenses
                
print("Within budget")
print("Amount remaining:", remaining, "naira")

if total_expenses == budget:
    print("Exactly on budget")
print("Amount remaining: 0 naira")
else: exceeded = total_expenses - budget
 print("Over budget")
    print("Amount exceeded:", exceeded, "naira")
                                   
#String is used when typing texts like names, addresses etc
#Float is used for numbers that contain decimal places
#Integer (int) is used for whole numbers without decimal numbers

#PSUEDOCODE
#BEGIN
 #INPUT student name
 #INPUT daily transport cost
 #INPUT daily feeding cost
 #INPUT other weekly expenses

 #transport total = daily transport cost * days on campus
 #feeding total = daily feeding cost * days on campus
 #weekly total = transport total + feeding total + Other weekly expenses

 #DISPLAY student name
 #DISPLAY transport total
 #DISPLAY feeding total
 #DISPLAY other weekly expenses
 #DISPLAY weekly total

#STOP

#Input: Student name, daily transport cost, daily feeding cost, days on campus, other expenses
#Process: Multiply daily transport cost by days on campus, add all expenses, Multiply daily feeding cost by days on campus
#Output: Transport total, feeding total, other expenses and weekly total
