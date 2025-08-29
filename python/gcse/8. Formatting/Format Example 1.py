# Layout example
# Global Variables
seeds =[["Radish",100,1.20],["Beetroot",200,1.35],["Courgette",50,2.45],["Carrot",300,1.99],["Parsnip",60,2.55]]
line="|"

# Main Program

for packet in seeds:
    seedName=packet[0]
    seedNum=packet[1]
    seedCost=packet[2]
    
    layout = "{:<10}{:>5}{:>5.2f}"
    
    print(layout.format(seedName,seedNum,seedCost))