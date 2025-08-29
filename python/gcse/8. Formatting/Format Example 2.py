# Layout example 2 - Completed
# Global Variables

population=[["USA",300112319,0.50],["United Kingdom",65988820,0.34],
            ["India",1428627663,0.81],["Vietnam",98858950,0.68],["Peru",34354719,0.89],
            ["Saint Martin",32077,0.90]]
line="|"
country=""
countryPop=0
countryChange=0.0

# layout variable
layout = "{:<15}{}{:>15}{}{:>15.2f}"

# Main Program

# Table Heading
print("="*48)
print("Country         |Population     |% Annual Change")
print("="*48)

# Start for
for item in population:
    country = item[0]
    countryPop=item[1]
    countryChange=item[2]
    
    print (layout.format(country,line,countryPop,line,countryChange))
    #end for

print("="*48)