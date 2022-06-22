# """
#  *****************************************************************************
#    FILE:        functions.py
#
#    AUTHOR:      {Midori Knecht}
#
#    ASSIGNMENT:  Magic 8 Ball fortune teller and Eli's Shipping
#
#    DATE:         {06/22/2022}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# ELI's SHIPPING RATES
# Ground Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$1.50           |	$20.00
# Over 2 lb but less than or equal to 6 lb  |   $3.00           |	$20.00
# Over 6 lb but less than or equal to 10 lb |   $4.00           |	$20.00
# Over 10 lb                                |   $4.75           |	$20.00

# Ground Shipping Premium
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$0.00           |	$125.00
# Over 2 lb but less than or equal to 6 lb  |   $0.00           |	$125.00
# Over 6 lb but less than or equal to 10 lb |   $0.00           |	$125.00
# Over 10 lb                                |   $0.00           |	$125.00

# Drone Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$4.50           |	$0.00
# Over 2 lb but less than or equal to 6 lb  |   $9.00           |	$0.00
# Over 6 lb but less than or equal to 10 lb |   $12.00          |	$0.00
# Over 10 lb                                |   $14.25          |	$0.00

from random import randrange 

def fortune(name, question):
  answer = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again       later.", "Better not tell you now.", "My soures say no.", "Outlook not so good.", "Very doubtful."]
  randAns = randrange(0, 9)
  fortune = answer[randAns]

  space = name.find(" ")
  fName = name[:space]

  if (fName[-1] == "s"):
    print(f"{fName}' Question: {question}")
  else:
    print(f"{fName}'s Question: {question}")
  
  print(f"Magic 8-Ball's answer: {fortune}")
  print()


def shipping(weight):
  if (weight <= 2):
    groundShip = weight * 1.5 + 20
    groundPremShip = 125
    droneShip = weight * 4.5
  elif (weight > 2 and weight <= 6):
    groundShip = weight * 3 + 20 
    groundPremShip = 125
    droneShip = weight * 9
  elif (weight > 6 and weight <= 10):
    groundShip = weight * 4 + 20 
    groundPremShip = 125
    droneShip = weight * 12
  else:
    groundShip = weight * 4.75 + 20 
    groundPremShip = 125
    droneShip = weight * 14.25
    
  print(f"The price of ground shipping is ${groundShip}.")
  print(f"The price of ground shipping is ${groundPremShip}.")
  print(f"The price of drone shipping is ${droneShip}.")

  if (groundShip < groundPremShip and groundShip < droneShip):
    best = "ground shipping"
  elif (groundPremShip < groundShip and groundPremShip < droneShip):
    best = "ground premium shipping"
  elif (groundShip == groundPremShip and groundShip < droneShip):
    best = "ground shipping or ground shipping premium"
  elif (droneShip == groundShip and droneShip < groundPremShip): 
    best = "drone shipping or ground shipping"
  elif (droneShip == groundPremShip and droneShip < groundShip):
    best = "drone shipping or ground premium shipping"
  else:
    best = "drone shipping"

  print(f"To save the most money you should use {best}.")

def main():
# fortune
  usersName = input("What's your name? ")
  usersQuestion = input("What's your question? ")
  fortune(usersName, usersQuestion)

# shipping
  packageWeight = float(input("How much does your package weigh in lbs? "))
  shipping(packageWeight)
    # Collect user input in main and pass these values to the functions fortune and shipping. 
    

##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()