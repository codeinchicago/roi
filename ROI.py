"""
Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
"""

#Check for valid input. How to do so with string input turned into an integer? I cannot check the string input b/c it is not an integer. Use isdigit().
#Make sure no divide by 0 errors with percent function
#Tidy it up.
#Put percentages on final calculation, limit it to {.2f}
#Do NPV, IRR

import time

class Rental():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.annual_cashflow = 0


    def income(self):
        rental = input("What is the rent? ")
        while rental.isdigit() != True:
            rental = input("What is the rent? ")
        rental = int(rental)

        laundry = input("What is the laundry income? ")
        while laundry.isdigit() != True:
            laundry = input("What is the laundry income? ")
        laundry = int(laundry)
        
        storage = input("What is the storage fee? ")
        while storage.isdigit() != True:
            storage = input("What is storage fee? ")
        storage = int(storage)

        misc = input("What is the miscellaneous income? ")
        while misc.isdigit() != True:
            misc = input("What is the miscellaneous income? ")
        misc = int(misc)

        self.monthly_income = rental + laundry + storage + misc
        print(f'Your income is: {self.monthly_income}.')
        return self.monthly_income

    def expenses(self):
        taxes = input("What are the taxes? ")
        while taxes.isdigit() != True:
            taxes = input("What are the taxes? ")
        taxes = int(taxes)

        insurance = input("How much for insurance? ")
        while insurance.isdigit() != True:
            insurance = input("How much for insurance? ")
        insurance = int(insurance)

        water = input("How much for sewage? ")
        while water.isdigit() != True:
            water = input("How much for sewage? ")
        water = int(water)

        utilities = input("How much for utilities? ")
        while utilities.isdigit() != True:
            utilities = input("How much for utilities? ")
        utilities = int(utilities)
        
        hoa = input("How much for homeowner association fees? ")
        while hoa.isdigit() != True:
            hoa = input("How much for homeowner association fees? ")
        hoa = int(hoa)
        
        self.monthly_expenses = taxes + insurance + water + utilities + hoa
        #print(f'Your expenses are: {self.monthly_expenses}.')
        return self.monthly_expenses

    def cashflow(self, monthly_income, monthly_expenses):
        #print(f'Inside cashflow, here is the income: {self.monthly_income}')
        monthly_cashflow = self.monthly_income - self.monthly_expenses
        self.annual_cashflow = monthly_cashflow * 12
        print(self.annual_cashflow)
        return self.annual_cashflow

    def percent(self, annual_cashflow):
        down = input("How much for down payment? ")
        while down.isdigit() != True:
            down = input("Please enter an integer. How much for down payment? ")
        down = int(down)

        closing = input("How much for closing costs? ")
        while closing.isdigit() != True:
            closing = input("Please enter an integer. How much for closing costs? ")
        closing = int(closing)

        rehab = input("How much for rehabilitation? ")
        while rehab.isdigit() != True:
            rehab = input("Please enter an integer. How much for rehabilitation? ")
        rehab = int(rehab)

        other = input("How much for other investment costs? ")
        while other.isdigit() != True:
            other = input("Please enter an integer. How much for other investment costs? ")
        other = int(other)

        investment = down + closing + rehab + other
        increase = self.annual_cashflow / investment
        print("Calculating your profit.")
        time.sleep(2)
        print("Factoring in market conditions, analyzing legislative environment.")
        time.sleep(2)
        #print(increase)
        percent = increase * 100
        print(f'{percent:.2f}% annual return on investment.')
        return percent

    def runit(self):
        print("All inputs are monthly and in integer form.")
        self.income()
        self.expenses()
        self.cashflow(self.monthly_income, self.monthly_expenses)
        self.percent(self.annual_cashflow)

rental = Rental()
rental.runit()