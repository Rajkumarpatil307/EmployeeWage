import random

class Employee:
    def __init__(self, wage_per_hour=20):
        self.wage_per_hour = wage_per_hour
        self.total_wage = 0
        self.total_hours = 0
        self.working_days = 0

    def calculate_wages_until_condition(self, max_hours=100, max_days=20):
        while self.total_hours < max_hours and self.working_days < max_days:
            attendance = random.randint(0, 2)
            
            if attendance == 1:
                self.total_wage += self.wage_per_hour * 8
                self.total_hours += 8
                self.working_days += 1
            elif attendance == 2:
                self.total_wage += self.wage_per_hour * 4
                self.total_hours += 4
                self.working_days += 1
            else:
                self.working_days += 1  # Counting days even if absent
        
        print(f"Total Wage: {self.total_wage}")
        print(f"Total Hours Worked: {self.total_hours}")
        print(f"Total Days Worked: {self.working_days}")

# Create an employee instance and calculate wages
employee = Employee()
employee.calculate_wages_until_condition()