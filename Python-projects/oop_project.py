# Project to develop a script that will allow the HR team to quickly analyze
# the bonus and vacation based on some known parameters

class Employee:
    def __init__(self, name, department, salary, bonus_percentage, years_of_service, retirement_contribution):
        self.name = name
        self.department = department
        self.salary = self.validate_salary(salary)
        self.bonus = self.calculate_bonus(bonus_percentage)
        self.vacation = self.calculate_vacation(years_of_service)
        self.retirement_contribution = self.validate_retirement_contribution(retirement_contribution)
        self.employer_contribution = self.retirement_contribution / 2

    def validate_salary(self, salary):
        if 45000 <= salary <= 125000:
            return salary
        else:
            return ValueError('salary must be between £45,000 and £125,000')
        
    def calculate_bonus(self, bonus_percentage):
        if 10 <= bonus_percentage <= 20:
            return self.salary * (bonus_percentage / 100)
        else:
            return ValueError('bonus percentage must be between 10''% ''and 20''%')
    
    def calculate_vacation(self, years_of_service):
        base_vacation = 2 * 52  # 2 hours per week for 52 weeks
        if years_of_service == 1:
            return base_vacation * 1.10
        elif years_of_service == 2:
            return base_vacation * 1.20
        elif years_of_service == 3:
            return base_vacation * 1.30
        elif years_of_service == 4:
            return base_vacation * 1.40
        elif years_of_service == 5:
            return base_vacation * 1.50
        else:
            return base_vacation
        
    def validate_retirement_contribution(self, contribution):
        if 0 <= contribution <= 0.10:
            return self.salary * contribution
        else:
            return ValueError('retirement contribution must be between 0''% ''and 10''%')

def main():
    employees = [
        Employee('John Doe', 'Finance', 50000, 15, 1, 0.05),
        Employee('Jane Smith', 'Marketing', 60000, 12, 2, 0.07),
        Employee('Mike Johnson', 'IT', 70000, 18, 3, 0.10)
    ]

    print(' Employee Bonus and Vacation Analysis '.center(50, '-'))

    for employee in employees:
        bonus_percentage = (employee.bonus / employee.salary) * 100
        vacation_percentage = (employee.vacation / (2 * 52)) * 100  # total vacation hours as percentage

        print(f'Employee: {employee.name}')
        print(f'Department: {employee.department}')
        print(f'Salary: ${employee.salary:,.2f}')  # .2f for decimal point 
        print(f'Bonus: ${employee.bonus:,.2f} ({bonus_percentage:.2f}%)')
        print(f'Vacation: {employee.vacation:,.2f} hours / {employee.vacation / 24:,.2f} days ({vacation_percentage:.2f}%)')
        print(f'Retirement Contribution: {employee.retirement_contribution:.2f}')
        print(f'Employer Contribution: {employee.employer_contribution:.2f}')
        print('--------------------')

    print(' Total Bonus and Vacation Analysis '.center(50, '-'))

    total_bonus = sum([employee.bonus for employee in employees])
    total_vacation = sum([employee.vacation for employee in employees])
    total_salary = sum([employee.salary for employee in employees])
    total_bonus_percentage = (total_bonus / total_salary) * 100
    total_vacation_percentage = (total_vacation / (2 * 52 * len(employees))) * 100

    print(f'Total Salary: ${total_salary:,.2f}')
    print(f'Total Bonus: ${total_bonus:,.2f} ({total_bonus_percentage:.2f}%)')
    print(f'Total Vacation: {total_vacation:.2f} hours ({total_vacation_percentage:.2f}%)')
    print('--------------------')

if __name__ == '__main__':
    main()
