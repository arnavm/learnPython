# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

naturals = range(1000) # All natural numbers from 1 to 1000
total = 0 # The running total of all multiples of 3 or 5
for number in naturals: # Iterate over all the natural numbers
    if number % 3 == 0 or number % 5 == 0: # If number is divisible by three or five...
        total += number # ...add it to the running total
print total # Report the sum

# 100,000 repetitions of the above code took 21.738 seconds