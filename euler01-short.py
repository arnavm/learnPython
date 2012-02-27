# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# The following code uses a list comprehension to efficiently generate
# the list of numbers less than 1000 that are multiples of 3 or 5.

print sum([number for number in range(1000) if number % 3 == 0 or number % 5 == 0])

# 100,000 repetitions of the above code took 21.415 seconds