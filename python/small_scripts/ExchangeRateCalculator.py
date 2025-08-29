#Dictionaries
CDN = {
    "CDN": 1,
    "GBP" : 1.71,
    "EUR" : 1.50,
    "JPY" : 0.0093,
    "USD" : 1.37
}

GBP = {
    "CDN" : 0.58,
    "GBP": 1,
    "EUR" : 0.88,
    "JPY" : 0.0054,
    "USD" : 0.80
}

EUR = {
    "CDN" : 0.67,
    "GBP": 1.14,
    "EUR" : 1,
    "JPY" : 0.0062,
    "USD" : 0.92
}

JPY = {
    "CDN" : 108.03,
    "GBP": 184.82,
    "EUR" : 161.90,
    "JPY" : 1,
    "USD" : 148.30
}

USD = {
    "CDN" : 0.73,
    "GBP": 1.25,
    "EUR" : 1.09,
    "JPY" : 0.0067,
    "USD" : 1
}

#Menu
def menu():
    print("Canadian dolars $ (CDN)")
    print("British pounds £ (GBP)")
    print("European euros € (EUR)")
    print("Japanese yen ¥ (JPY)")
    print("American dollars $ (USD)")
    print("Which currency do you want to convert from? ")
    global user_from
    global user_to
    global user_amount
    user_from = input()
    print()
    print("Which currency do you want to convert to? ")
    user_to = input()
    print()
    print("How amount of currency do you want to exchange: ")
    user_amount = input()
    user_amount = float(user_amount)
    print()
    return user_from, user_to, user_amount

#Long version
    #Sub-programs 

def cdn_calculations():
    global price
    if user_to == "CDN":
        print("Its the same currency!")
    if user_to == "GBP":
        price = user_amount * (CDN["GBP"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"GBP")
    if user_to == "EUR":
        price = user_amount * (CDN["EUR"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"EUR")
    if user_to == "JPY":
        price = user_amount * (CDN["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"JPY")    
    if user_to == "USD":
        price = user_amount * (CDN["USD"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"USD")

def gbp_calculations():
    global price       
    if user_to == "CDN":
        price = user_amount * (GBP["CDN"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"CDN")
    if user_to == "GBP":
        print("Its the same currency!")
    if user_to == "EUR":
        price = user_amount * (GBP["EUR"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"EUR")
    if user_to == "JPY":
        price = user_amount * (GBP["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"JPY")    
    if user_to == "USD":
        price = user_amount * (GBP["USD"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"USD")

def eur_calculations():
    global price
    if user_to == "CDN":
        price = user_amount * (EUR["CDN"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"CDN")
    if user_to == "GBP":
        price = user_amount * (EUR["GBP"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"GBP")
    if user_to == "EUR":
        print("Its the same currency!")
    if user_to == "JPY":
        price = user_amount * (EUR["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"JPY")    
    if user_to == "USD":
        price = user_amount * (EUR["USD"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"USD")

def jpy_calculations():
    global price
    if user_to == "CDN":
        price = user_amount * (JPY["CDN"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"CDN")
    if user_to == "GBP":
        price = user_amount * (JPY["GBP"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"GBP")
    if user_to == "EUR":
        price = user_amount * (JPY["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"EUR")  
    if user_to == "JPY":
        print("Its the same currency!")  
    if user_to == "USD":
        price = user_amount * (JPY["USD"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"USD")

def usd_calculations():
    global price
    if user_to == "CDN":
        price = user_amount * (USD["CDN"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"CDN")
    if user_to == "GBP":
        price = user_amount * (USD["GBP"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"GBP")
    if user_to == "EUR":
        price = user_amount * (USD["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"EUR")  
    if user_to == "JPY":
        price = user_amount * (USD["JPY"])
        price = price * 1.01
        print("Do you want to exchange",user_amount,user_from,"for",price,"JPY")
    if user_to == "USD":
        print("Its the same currency!")  

#Main program

menu()

if user_from == "CDN":
    cdn_calculations()

if user_from == "GBP":
    gbp_calculations()

if user_from == "EUR":
    eur_calculations()

if user_from == "JPY":
    jpy_calculations()

if user_from == "USD":
    usd_calculations()

user_input = input()
if user_input == "yes":
    print("You have successfully exchanged the money.")


print("Have a good day!")