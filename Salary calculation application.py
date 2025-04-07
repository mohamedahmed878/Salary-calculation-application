# Add job salary 
salary = input("Please enter the job salary: ") 
salary = int(salary)

# Add day 30 
days = 30 

# salary / days 30 
day_salary = salary / days 

# If the month is completed, a bonus of 1000 will be added
bonus = 1000

# Ask if the employee completed the month
answer = input("Has the employee completed the month? (True/False): ")

# Handle lowercase input safely
if answer.lower() == "true":
    total_salary = salary + bonus
    print("The employee has completed the month. Total salary with bonus is: " + str(total_salary))
elif answer.lower() == "false":
    print("The employee has not completed the month.")
    days_worked = input("Please enter how many working days the employee completed: ")
    days_worked = int(days_worked)
    calculated_salary = day_salary * days_worked
    print("The calculated salary is: " + str(calculated_salary))
else:
    print("Please enter the data correctly (True or False only)")
