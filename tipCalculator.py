# Write a program that takes as input the cost of a meal. Then, tell the user what 15% tip would be ("Fifteen percent tip for this meal is ____") and what the total cost will be ("This meal costs ___ in total").

cost = float(raw_input("Cost of your meal: ")) # Convert the input string to a float
print "Fifteen percent tip for this meal is $%.2f" % (cost * 0.15) # Calculate and print the tip
print "This meal costs $%.2f in total" % (cost * 1.15) # Calculate and print the total cost
print # An extra newline for aesthetics