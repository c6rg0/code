import random
highscore = 0
hs_name = 0

print("        Mastermind game")
print()
print("Current highscore:",highscore,"by",hs_name) 
print()
print("Choose a difficulty and enter its corresponding number:")
print("1.Easy")
print("2.Normal")
print("3.Difficult")
difficulty = int(input(""))

if difficulty == 1:
    print("Easy difficulty is chosen.")
    print()
    number = random.randint(1000,9999)
    guess = 0
    tries = 0

    while guess != number:
        guess = int(input("Guess a four digit number: "))
        tries = tries + 1
    
        if number != guess:
            print("Wrong, you have tried",tries,"times.")

            if guess < number:
                print("Guess is larger")
                print()

            if guess > number:
                print("Guess is smaller")
                print()
                    
                
        if number == guess:
            print("Well done, it had took you",tries,"tries.")

            if guess < highscore:
                hs_name = input("What is your name")
                print("Congratulations!!!, you got a highscore of",guess)
                highscore = guess


if difficulty == 2:
    print("Normal difficulty is chosen.")
    print()
    number = random.randint(1000,9999)
    guess = 0
    tries = 0

    while guess != number:
        guess = input("Guess a four digit number: ")
        guess = int(guess)
        tries = tries + 1
    
        if number != guess:
            print("Wrong, you have tried",tries,"times.")
                
        if number == guess:
            print("Well done, it had took you",tries,"tries.")

            if guess < highscore:
                hs_name = input("What is your name")
                print("Congratulations!!!, you got a highscore of",guess)
                highscore = guess



if difficulty == 3:
    print("Hard difficulty is chosen.")
    print()
    number = random.randint(10000,99999)
    guess = 0
    tries = 0

    while guess != number:
        guess = input("Guess a five digit number: ")
        guess = int(guess) 
        tries = tries + 1
    
        if number != guess:
            print("Wrong, you have tried",tries,"times.")
                
        if number == guess:
            print("Well done, it had took you",tries,"tries.")

            if guess < highscore:
                hs_name = input("What is your name")
                print("Congratulations!!!, you got a highscore of",guess)
                highscore = guess




