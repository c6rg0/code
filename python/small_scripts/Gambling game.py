import random
balance = 1000
bet = 0

def menu():
    global bet
    global balance
    print("You can bet for a number 0 to 30: ")
    print("if it's an odd number, you get 2x money back,")
    print("if it's a number under 5, you get 5x your money back,")
    print("if it's even you lose all of you bet,")
    print("and if the number is 0 you lose 2x of your bet")
    print()

def game():
    print("Your bank balance is",balance)
    bet = int(input("How much money do you want to bet? "))
    if bet < 0:
        print("You can't bet £0")
    print()

    num = random.randint(0,30)

    if num * 2 & 5:
        reward = bet * 2
        print("You won £",reward," because the number was odd!")
        balance = balance + (bet * 2)

    if 0 < num <= 5:
        reward = bet * 5
        print("You won £",reward," because the number was less than 5!")
        balance = balance + (bet * 5)

    if num * 2 & 0:
        print("You lost £",bet," because the number was even :( ")
        bet = 0

    if num == 0:
        print("You have lost £",bet*2,":( ")
        balance = balance - (bet*2)



menu()
game()

again = input("Do you want to pay again or not? ")
while again != "n" or "no":
    menu()
    game()