#----------------------------
# Sandwich orders program
#----------------------------
MAX_BOXES = 5

#----------------------------
# Global variables
#----------------------------
boxes = ["circle", "square", "triangle", "hexagon", "octagon"]

#----------------------------
#Subprograms
#----------------------------
def isValid(pLocation):
    valid = False

    if(pLocation - 1 >=0) and (pLocation - 1 <MAX_BOXES):
        valid = True
    return (valid)

def showBox (pLocation):
    theString = ""

    theString = "The box is " + boxes[pLocation - 1] + " shaped"
    print (theString)

#-------------------------
#Main program
#-------------------------
choice = int(input("Welcome to the game.  Choose a number (1 to 5) "))
if (isValid (choice)):
    showBox (choice)
else:
    print ("Invalid choice")
