import random

class EmployeeWageComputation:
    @classmethod
    def calculate_wages(cls, company, wage_per_hour, max_hours, max_days):
        total_wage = 0
        total_hours = 0
        working_days = 0

        while total_hours < max_hours and working_days < max_days:
            attendance = random.randint(0, 2)

            match attendance:
                case 1:
                    total_wage += wage_per_hour * 8
                    total_hours += 8
                    working_days += 1
                case 2:
                    total_wage += wage_per_hour * 4
                    total_hours += 4
                    working_days += 1
                case _:
                    pass

        print(f"Company: {company}")
        print(f"Total Wage: {total_wage}")
        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Days Worked: {working_days}")
        print("-" * 30)

EmployeeWageComputation.calculate_wages("Company A", 20, 100, 20)
EmployeeWageComputation.calculate_wages("Company B", 25, 120, 22)
EmployeeWageComputation.calculate_wages("Company C", 18, 90, 18)