class RentalProperty():
    def __init__(self, income, expenses, cash_flow, roi):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.roi = roi



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



class Expenses():
    def __init__(self, tax, insurance, utilities, hoa, lawn, snow, vacency,
    repairs, capEx, property_management, mortgage):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn = lawn
        self.snow = snow
        self.vacency = vacency
        self.repairs = repairs
        self.capEx = capEx
        self.property_management = property_management
        self.mortgage = mortgage

    def taxes(self):
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
        
        total_monthly_expenses = round(monthly_expenses, 2)
        return total_monthly_expenses
        



class CashFlow():
    def __init__(self):

        def the_cash_flow():
            total_monthly_cash_flow = total_monthly_income - total_monthly_expenses



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



