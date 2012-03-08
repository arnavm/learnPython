# Code will consist of multiple blocks
# First block will assemble a List containing the Fibonacci sequence starting with terms 1 and 2 and ending before the last term exceeds 4 million
# Second block will find the sum of the even valued terms in the FS List


# BLOCK 1 #
# Assemble a List containing the Fibonacci sequence with values not exceeding 4 million #

FS = [1,2]  # Define a List to contain the Fibonacci sequence initially containing the terms 1 and 2
while FS[-1] < 4000000:  # continue appending to the FS List each time the last term is less than 4 million, by
	FS.append(FS[-1] + FS[-2])  # grow the FS list by 1 term at a time with each new term being the sum of the previous terms
if FS[-1] > 4000000: # if the last term in the FS List is > 4000000,
	del FS[-1]  # then delete it
print FS # optional step
print


# BLOCK 2 #
# Sum of the even valued terms in the FS List generated above #

FSeven = []  # Create a new List
for x in FS:  # containing only the even numbers from the FS List (go through each of the terms in the FS List and add them to the FSeven List if it is even)
	if x %2 == 0:
		FSeven.append(x)
print FSeven 
print sum(FSeven)  # add the numbers in the List generated above and print them
print

