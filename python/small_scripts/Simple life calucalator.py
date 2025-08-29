#Simple life calucalator
calculator = 0

value1 = 0
value2 = 0
result = 0

print("Simple life calculator")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("Which caluclator do you want to use (enter a number)? ")
print("Vat (1)")
print("Tax (2)")
print("Times table (3)")
calculator = input()
print()
    
def vat():

    vat = 0
    price = 0
    vat_rate = 0 
    price_bv = 0

    vat = input("Do you need to calculate exclusive (1), or inclusive (2) VAT? ")
    
    if vat == 1:
        price = input("Enter the price: ")
        price = int(price)
        vat_rate = input("Enter the VAT rate: ")
        vat_rate = int(vat_rate)
        vat_rate = (100 + vat_rate)/100
        price_bv = price / vat_rate
        print("The price with the tax is now",price_bv)

    if vat == 2:    # Tax already factored into the price, you are removing the tax from the price.
        price = input("Enter the price: ")
        price = int(price)
        vat_rate = input("Enter the VAT rate: ")
        vat_rate = int(vat_rate)
        vat_rate = (100 - vat_rate)/100
        price_bv = price * vat_rate
        print("The price without the tax is now",price_bv)

def tax():

    income = 0
    tax_rate = 0
    t_income = 0
    tax = 0
    
    income = input("What is your yearly income? ")
    income = int(income)   

    if income <= 12570:
        tax_rate = 0
        print("You don't have to pay taxes")

    if 12571 >= income >= 50270:
        tax_rate = 0.20
        tax = income * tax_rate
        t_income = income - tax
        print("You have £",tax,"of tax, and you have £",t_income," left over.")

    if 50271 >= income >= 125140:
        tax_rate = 0.40
        tax = income * tax_rate
        t_income = income - tax
        print("You have £",tax,"of tax, and you have £",t_income," left over.")

    if income >= 125140:
        tax_rate = 0.45
        tax = income * tax_rate
        t_income = income - tax
        print("You have £",tax,"of tax, and you have £",t_income," left over.")

def tt():
    print("You have picked timestable,")
    value1 = input("What is the first value? ")
    value2 = input("What is the second value? ")
    value1 = int(value1)
    value2 = int(value2)   

    result = value1 * value2
    print(value1,"x",value2,"=",result)

    if calculator == 1:
        vat()

    if calculator == 2:
        vat()

    if calculator == 3:
        vat()


