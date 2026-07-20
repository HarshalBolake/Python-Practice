class Employee:
    def __init__(self,name,basicSalary):
        self.name = name
        self.basic_salary = basicSalary
        self.coding_bonus_amount = 0
        self.management_bonus_amount = 0
    
    def show_salary(self):
        print(f"Basic Salary: {self.basic_salary}")

class Developer(Employee):
    def coding_bonus(self,bonus_amount):
        self.coding_bonus_amount = bonus_amount
        print(f"Coding Bonus: {bonus_amount}")

class Manager(Employee):
    def Management_bonus(self,bonus_amount):
        self.management_bonus_amount = bonus_amount
        print(f"Management Bonus: {bonus_amount}")

class TeamLead(Developer,Manager):
    def total_salary(self):
        self.total_salary = self.basic_salary + self.coding_bonus_amount + self.management_bonus_amount
        print(f"Total salary: {self.total_salary}")

TL1 = TeamLead("Harshal",50000)
TL1.show_salary()
TL1.coding_bonus(5000)
TL1.Management_bonus(7000)
TL1.total_salary()