# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
lastName = ""
firstName = ""
dob = ""
myID = ""

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# =====> Change the names of the local variables to distinguish them
#        from the global variables with the same name
def makeID (lastName, firstName, dob):
    namePart = ""
    numberPart = 0

    namePart = lastName + firstName[0]  # Letter part

    # =====> Correct the logic error caused by using the int() function
    #        in the number part calculation rather than using a function
    #        that returns the ASCII value of the character
    for character in dob:
        numberPart = numberPart + int (character)

    yourID = namePart + str (numberPart)

    return (yourID)

# =====> Add a procedure, with no parameters, to display a
#        welcome message for the user

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Call the welcome procedure before taking input from the user

# Get last name and first name from the user
lastName = input ("Enter your last name: ")
firstName = input ("Enter your first name: ")

# =====> Convert last name and first name to lowercase after they
#        are inputted by the user

# Get date of birth from the user
dob = input ("Enter your date of birth (ddmmyyyy): ")

# =====> Check that only the digits 0 to 9 appear in the date of birth

# =====> Call the makeID() function, if the date of birth is valid
myID = makeID (lastName, firstName, dob)
print (myID)

# =====> Tell the user, if the date of birth is invalid
