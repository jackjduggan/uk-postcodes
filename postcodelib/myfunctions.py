"""
Postcodes are:
- alphanumeric
- variable in length (6-8 chars including space)
- divided into 2 parts separated by space (outward, inward)
"""

def isNumber(char):
    numbers = list(range(0,10))
    if char in numbers:
        return True
    else:
        return False
    

sample_postcode = "EC1A 1BB"
sliced_postcode = []
sliced_postcode[:] = sample_postcode # https://www.geeksforgeeks.org/python-splitting-string-to-list-of-characters/

print(sliced_postcode)
# returns: ['E', 'C', '1', 'A', ' ', '1', 'B', 'B']

def checkEachChar(list):
    for char in list:
        isNumber(char)
    
checkEachChar(sliced_postcode)