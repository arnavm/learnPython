# Find the greatest product of five consecutive digits in the 1000-digit number.
# 
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450

# This function multiplies two numbers together
from operator import mul

# Open the file containing this number and read its contents into a variable
f = open('euler08file.txt', 'r')
# f.read() instead of f.readlines() because we want one string containing the entire number
number = f.read()
f.close() # Close the file because we are done using it

# Since the file contains 50 digits per line, 
# we have to concatenate the lines into a single 1000 chacter string
number = number.replace('\n', '')
# Now let's convert this string to a list. That way, each digit is a separate element.
number = list(number)
# However, now every element is a string containing a single digit. We can't multiply
# two strings (e.g. '5' * '6' makes no sense), so we need to convert each element to an int
number = [int(elem) for elem in number]

# Initialize our variables. greatestProduct is 0 because we haven't found
# any products yet. The starting and ending indices allow us to slice the 
# first five digits in the number.
greatestProduct = 0
startingIndex = 0
endingIndex = 5

# Go through the number five digits at a time, sliding over one digit every
# iteration of the loop.
while endingIndex != len(number):
    digits = number[startingIndex:endingIndex] # This is our substring
    # The reduce function applies a function to an iterable. In this case,
    # it multiplies all the numbers in the list digits together, giving us our product
    product = reduce(mul, digits)
    # If product is larger than our greatestProduct, make greatestProduct equal to product
    if product > greatestProduct:
        greatestProduct = product
    # Slide over one digit to the next set of 5 consecutive digits
    startingIndex += 1
    endingIndex += 1

# Return our answer
print greatestProduct