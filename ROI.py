"""
Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
"""

#Check for valid input.
#Make sure no divide by 0 errors with percent function
#Tidy it up.

class Rental():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.annual_cashflow = 0


    def income(self):
        rental = int(input("What is the rent? "))
        laundry = int(input("What is the laundry income? "))
        storage = int(input("What is the storage fee? "))
        misc = int(input("Enter miscellaneous income. "))
        self.monthly_income = rental + laundry + storage + misc
        print(f'Your income is: {self.monthly_income}.')
        return self.monthly_income

    def expenses(self):
        taxes = int(input("What are the taxes? "))
        insurance = int(input("How much for insurance? "))
        water = int(input("How much for sewage? "))
        utilities = int(input("How much for utilities? "))
        hoa = int(input("How much for homeowner association fees? "))
        self.monthly_expenses = taxes + insurance + water + utilities + hoa
        print(f'Your expenses are: {self.monthly_expenses}.')
        return self.monthly_expenses

    def cashflow(self, monthly_income, monthly_expenses):
        print(f'Inside cashflow, here is the income: {self.monthly_income}')
        monthly_cashflow = self.monthly_income - self.monthly_expenses
        self.annual_cashflow = monthly_cashflow * 12
        print(self.annual_cashflow)
        return self.annual_cashflow

    def percent(self, annual_cashflow):
        down = int(input("How much for down payment? "))
        closing = int(input("How much for closing costs? "))
        rehab = int(input("How much for rehabilitation? "))
        other = int(input("How much for other investment costs? "))
        investment = down + closing + rehab + other
        
        increase = self.annual_cashflow / investment
        print(increase)
        percent = increase * 100
        print(percent)
        return percent

    def runit(self):
        self.income()
        self.expenses()
        #print("Test" + str(self.monthly_income))
        self.cashflow(self.monthly_income, self.monthly_expenses)
        self.percent(self.annual_cashflow)

#income()
#expenses()
#cashflow(212,12)
#percent(100)

rental = Rental()
rental.runit()