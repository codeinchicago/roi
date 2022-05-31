"""
Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
"""


import time

class Rental():

    def income(self):
        rental = input("What is the rent? ")
        while rental.isdigit() != True:
            rental = input("Please enter an integer. What is the rent? ")
        rental = int(rental)

        laundry = input("What is the laundry income? ")
        while laundry.isdigit() != True:
            laundry = input("Please enter an integer. What is the laundry income? ")
        laundry = int(laundry)
        
        storage = input("What is the storage fee? ")
        while storage.isdigit() != True:
            storage = input("Please enter an integer. What is the storage fee? ")
        storage = int(storage)

        misc = input("What is the miscellaneous income? ")
        while misc.isdigit() != True:
            misc = input("Please enter an integer. What is the miscellaneous income? ")
        misc = int(misc)

        self.monthly_income = rental + laundry + storage + misc
        print(f'\nYour monthly income is: ${self.monthly_income}.\n')
        return self.monthly_income

    def expenses(self):
        taxes = input("What are the taxes? ")
        while taxes.isdigit() != True:
            taxes = input("Please enter an integer. What are the taxes? ")
        taxes = int(taxes)

        insurance = input("How much for insurance? ")
        while insurance.isdigit() != True:
            insurance = input("Please enter an integer. How much for insurance? ")
        insurance = int(insurance)

        water = input("How much for sewage? ")
        while water.isdigit() != True:
            water = input("Please enter an integer. How much for sewage? ")
        water = int(water)

        utilities = input("How much for utilities? ")
        while utilities.isdigit() != True:
            utilities = input("Please enter an integer. How much for utilities? ")
        utilities = int(utilities)
        
        hoa = input("How much for homeowner association fees? ")
        while hoa.isdigit() != True:
            hoa = input("Please enter an integer. How much for homeowner association fees? ")
        hoa = int(hoa)
        
        self.monthly_expenses = taxes + insurance + water + utilities + hoa
        print(f'\nYour monthly expenses are: ${self.monthly_expenses}.')
        return self.monthly_expenses

    def cashflow(self, monthly_income, monthly_expenses):
        monthly_cashflow = self.monthly_income - self.monthly_expenses
        self.annual_cashflow = monthly_cashflow * 12
        print(f'\nYour annual cashflow is ${self.annual_cashflow}.\n')
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

        self.investment = down + closing + rehab + other
        increase = self.annual_cashflow / self.investment
        print("Calculating your profit.")
        time.sleep(2)
        print("Factoring in market conditions, analyzing legislative environment.")
        time.sleep(2)
        percent = increase * 100
        print(f'\n{percent:.2f}% annual return on investment.\n')
        return percent

    def irr(self, annual_cashflow, investment):
        discount = input("What discount rate should be used? ")
        while discount.isdigit() != True:
            discount = input("Please enter an integer. What discount rate should be used? ")
        discount = int(discount)

        viability = (self.annual_cashflow/(1+discount/100)) - self.investment
        print(f'The Internal Rate of Return is {viability:.2f}%.')


    def runit(self):
        print("Welcome to the Real Estate ROI Calculator.")
        print("All inputs are monthly and in integer form.")
        self.income()
        self.expenses()
        self.cashflow(self.monthly_income, self.monthly_expenses)
        self.percent(self.annual_cashflow)
        runirr = input('Press y to calculate an internal rate of return for one year. Note that result will often be unfavorable because of limited time span. ')
        if runirr == 'y':
            self.irr(self.annual_cashflow, self.investment)
        runagain = input('Press y to run the calculator again, any other key to exit. ')
        if runagain == 'y':
            Rental().runit()
        else:
            print("Quitting now. Good luck with your investment.")

rental = Rental()
rental.runit()