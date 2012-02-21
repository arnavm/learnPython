# Write a program that takes in a (space-delimited) list of names
# and reports to the user, "You entered these names:" 
# followed by the names (one per line) in alphabetical order. 
# The last line should tell the user how many names they entered, i.e. "You entered ____ names."

names = raw_input("Enter a list of names separated by a single space: ") # Helpful greeting message
names = names.strip().split(' ') # Eliminate any leading and trailing whitespace characters
names.sort(key = str.lower) # Case-insensitive sorting
print "You entered these names:\n%s" % '\n'.join(names) # The names, one per line
print "You entered %d name(s)" % len(names) # How many names did the user enter?
print # An extra newline for aesthetics