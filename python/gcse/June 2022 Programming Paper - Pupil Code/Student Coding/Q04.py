# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
layout = "{} is {}"
binary = ""
denary = 0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def binaryLoop (pBinary):
# =====> Rearrange the mixed up lines#
    digit = ""
    total = 0
    value = 0
    multiplier = 1
    
    for index in range (len (pBinary) - 1, -1, -1):
        digit = pBinary[index]
        value = multiplier * int (digit)
        total = total + value
        multiplier = multiplier * 2
    return (total)
# End of mixed up lines

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Rearrange the mixed up lines
binary = input ("Enter a binary pattern (empty to exit): ")
while (binary != ""):
    denary = binaryLoop (binary)
    print (layout.format (binary, denary))
    binary = input ("Enter a binary number (empty to exit): ")
# End of mixed up lines

