import random

def check_attendance():
    attendance = random.randint(0, 1)
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")

def calculate_daily_wage(wage_per_hour, full_day_hours):
    attendance = random.randint(0, 1)
def calculate_daily_wage(wage_per_hour):
    attendance = random.randint(0, 2)  # 0: Absent, 1: Full-time, 2: Part-time
    
    if attendance == 1:
        daily_wage = wage_per_hour * full_day_hours
        print(f"Employee is Present. Daily Wage: {daily_wage}")
        daily_wage = wage_per_hour * 8  # Full-time hours
        print(f"Employee is Present (Full-time). Daily Wage: {daily_wage}")
    elif attendance == 2:
        daily_wage = wage_per_hour * 4  # Part-time hours
        print(f"Employee is Present (Part-time). Daily Wage: {daily_wage}")
    else:
        print("Employee is Absent. Daily Wage: 0")


check_attendance()
calculate_daily_wage(20, 8)
calculate_daily_wage(20) 