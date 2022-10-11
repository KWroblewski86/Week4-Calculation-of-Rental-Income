class RentalProperty():
    # this is a good start but we're going to take the parameters out of instantiation so we don't have to have that data right away.  The choices are perfect tho!
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.roi = 0
        #I used 0's here but you could just as easily do None or whatever.  We know we're gonna need them but don't know what they are yet.


# MAKE THIS A METHOD!!!!
class Income():
    def __init__(self, rental, laundry, storage, other):
        self.rental = rental
        self.laundry = laundry
        self.storage = storage
        self.other = other

    def rentalIncome(self):
        monthly_income = input("What is your total monthly income?: ")
        total_monthly_income = int(monthly_income)
        print(total_monthly_income)
#
#I'm going to modify the Expenses class to a method to show you what I mean!\/ \/ \/ 

# MAKE THIS A METHOD!!!!

    def expense(self):
        
        tax = input("Please enter the amount of your taxes: ")
        tax_float = float(tax)

        insurance = input("Please enter the amount your insurance: ")
        insurance_float = float(insurance)

        utilities = input("Pleae enter the amount of your utilities: ")
        utilities_float = float(utilities)

        hoa = input("Please enter any HOA fees you may have: ")
        hoa_float = float(hoa)

        lawn = input("Please enter any lawn fees you may have: ")
        lawn_float = float(lawn)

        snow = input("Please enter any snow fees you may have: ")
        snow_float = float(snow)

        vacency = input("Please enter any vacency fees you may have: ")
        vacency_float = float(vacency)

        repairs = input("Please enter the amount of your repairs: ")
        repairs_float = float(repairs)

        capEx = input("Please enter the amount of your capital expenses: ")
        capEx_float = float(capEx)

        prop_management = input("Please enter any property management fees you have: ")
        prop_management_float = float(prop_management)

        mortgage = input("Please enter the mortgage on the property: ")
        mortgage_float = float(mortgage)

        monthly_expenses = tax_float + insurance_float + utilities_float + hoa_float + lawn_float
        + snow_float + vacency_float + repairs_float + capEx_float + prop_management_float + mortgage_float
        
        self.expenses = monthly_expenses
        print(f'Your updated monthly expenses total- ${self.expenses}')
        


# MAKE THIS A METHOD!!!!
class CashFlow():
    def __init__(self):

        def the_cash_flow():
            total_monthly_cash_flow = total_monthly_income - total_monthly_expenses


# MAKE THIS A METHOD!!!!
class ReturnOnInvestment():
     def __init__(self):

        def cash_on_cash_roi():
            down_payment = input(int("How much was the down payment on your property?: "))
            closing_cost = input(int("How much were the closing costs?: "))
            rehab = input(int("How much did you spend on rehab for the property?: "))
            misc = input(int("Were there any miscellaneous costs?: "))

            total_investment = down_payment + closing_cost + rehab + misc
            annual_cash_flow = total_monthly_cash_flow * 12
            cash_on_cash_return = annual_cash_flow / total_investment * 100
            print(cash_on_cash_return + "%")

#Finally we need to code to run this as a program!  in psuedo-code:
    #def run(self):
        #self.rental_income()
        # self.expense()
        # self.ROI()

#Last, instantiate the class and run it:
# x = RentalProperty()
# x.run()



