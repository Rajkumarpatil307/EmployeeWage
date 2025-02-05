import random

def check_attendance():
    attendance = random.randint(0, 1)
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")

def calculate_daily_wage(wage_per_hour, full_day_hours):
    attendance = random.randint(0, 1)
    if attendance == 1:
        daily_wage = wage_per_hour * full_day_hours
        print(f"Employee is Present. Daily Wage: {daily_wage}")
    else:
        print("Employee is Absent. Daily Wage: 0")
check_attendance()
calculate_daily_wage(20, 8)