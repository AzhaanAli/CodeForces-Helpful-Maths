# DIRECTIONS:
# Given a string containing a sum, for example "1+4+2+6", sort numbers to be in ascending order.
# The example would result in "1+2+4+6" for example.

userInput = input()

# Split input by + characters, then sort the list.
asList = userInput.split('+')
asList.sort()

# Create a string with the +'s between every element, and print.
asString = ''
for i in asList:
    asString += i + '+'

# Substring to remove the extra + at the end.
print(asString[0: len(asString) - 1])
