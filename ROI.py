"""
Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
"""

#Income
#Expenses
#Cash Flow
#Return
#Check for valid input.
#Make sure no divide by 0 errors with percent function


print("All amounts per month.")

def income():
    rental = int(input("What is the rent? "))
    laundry = int(input("What is the laundry income? "))
    storage = int(input("What is the storage fee? "))
    misc = int(input("Enter miscellaneous income. "))
    monthly_income = rental + laundry + storage + misc
    print(monthly_income)
    return monthly_income

def expenses():
    taxes = int(input("What are the taxes? "))
    insurance = int(input("How much for insurance? "))
    water = int(input("How much for sewage? "))
    utilities = int(input("How much for utilities? "))
    hoa = int(input("How much for homeowner association fees? "))
    monthly_expenses = taxes + insurance + water + utilities + hoa
    print(monthly_expenses)
    return monthly_expenses

def cashflow(monthly_income, monthly_expenses):
    monthly_cashflow = monthly_income - monthly_expenses
    annual_cashflow = monthly_cashflow * 12
    print(annual_cashflow)
    return annual_cashflow

def percent(annual_cashflow):
    down = int(input("How much for down payment? "))
    closing = int(input("How much for closing costs? "))
    rehab = int(input("How much for rehabilitation? "))
    other = int(input("How much for other investment costs? "))
    investment = down + closing + rehab + other
    
    increase = annual_cashflow / investment
    print(increase)
    percent = increase * 100
    print(percent)
    return percent

#income()
#expenses()
#cashflow(212,12)
#percent(100)