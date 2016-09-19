# set the initial values here

cost = 1
TotalCost = 0

# Provide instructions
print ("Input Prices. Enter 0 to finish.")

# the user will stay in the following loop until they enter the value 0
while cost != 0:
    strCost = raw_input("Enter the cost of the item: ")
    # a raw input is a string, after casting it to a float a new value for the cost will be saved
    cost = float(strCost)
    # This makes the Total cost equal to the original cost while also adding the new value
    TotalCost += cost
else:
    print ("The total is $" + str(TotalCost))

strTax = (TotalCost * .06)

taxAmount = TotalCost * .06
print("That is $" + str(round(taxAmount, 2)))
grandTotal = float(taxAmount) + TotalCost
# we have to cast grandTotal to a string to be able to print it
print("The total cost, with tip, is: $" + str(round(grandTotal, 2)))




