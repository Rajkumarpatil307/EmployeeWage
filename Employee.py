import random

def calculate_daily_wage(wage_per_hour):
    attendance = random.randint(0, 2)
    
    match attendance:
        case 1:
            daily_wage = wage_per_hour * 8
            print(f"Employee is Present (Full-time). Daily Wage: {daily_wage}")
        case 2:
            daily_wage = wage_per_hour * 4
            print(f"Employee is Present (Part-time). Daily Wage: {daily_wage}")
        case _:
            print("Employee is Absent. Daily Wage: 0")

def calculate_monthly_wage(wage_per_hour):
    total_wage = 0
    working_days = 20

    for _ in range(working_days):
        attendance = random.randint(0, 2)
        
        match attendance:
            case 1:
                total_wage += wage_per_hour * 8
            case 2:
                total_wage += wage_per_hour * 4
            case _:
                total_wage += 0
    
    print(f"Total Monthly Wage: {total_wage}")

# Function calls
calculate_daily_wage(20)
calculate_monthly_wage(20)
