characterRec = ""
story = 0

#gender
f = open("character.txt","w")
print("Choose the following")
gender = input("Do you want to be a man or a female? ")
gender = ("gender =",gender,"\n")
f.write = (gender)
f.close()
print()

#age
f = open("character.txt","a")
print("What age do you want to pick?")
print()
print("10 years old:")
print("+100 potential")
print("+70 inteligence")
print("0 abilities")
print("+5 physical strength")
print()
    
print("20 years old:")
print("+60 potential")
print("+90 inteligence")
print("+1 ability")
print("+50 physical strength")
print()

print("Choose which age: ")
age = input()
age = int(age)
    
if age == 10:
    f.write("age = 10 \n")
    f.write("potential = 100 \n")
    f.write("inteligence = 70 \n")
    f.write("ability = 0 \n")
    f.write("physical_strength = 5 \n")

story = 1
    f.write("story = 1")
    
if age == 20:
    f.write("age = 20 \n")
    f.write("potential = 60 \n")
    f.write("inteligence = 90 \n")
    f.write("ability = ? \n")
    f.write("physical_strength = 50 \n")
    f.close()

    story = 2
    f.write("story = 2")

    #ability decision

    print("You are wandering through a large forest, in the year 1500,")
    print("You can decide between the world cutting sword (1)")
    print("OR")
    print("The super speed? (2)")
    choice = input()
    choice = int(choice)

    if choice == 1:
        ability = "world cutting sword"
        story = 21

    if choice == 2:
        ability = "super speed"
        story = 22

    #story begins

    

    

    

    
    
        



    
        
    


    
