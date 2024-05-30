"""
Postcodes are:
- alphanumeric
- variable in length (6-8 chars including space)
- divided into 2 parts separated by space (outward, inward)
"""

def isNumber(c):
    return c.isdigit()
    

sample_postcode = "EC1A 1BB"
sliced_postcode = []
sliced_postcode[:] = sample_postcode # https://www.geeksforgeeks.org/python-splitting-string-to-list-of-characters/

print(sliced_postcode)
# returns: ['E', 'C', '1', 'A', ' ', '1', 'B', 'B']

def checkEachChar(list):
    for c in list:
        print(f"Checking: {c}")
        if isNumber(c) == True:
            print("True")
        else:
            print("False")
    
checkEachChar(sliced_postcode)

def formatCode(list):
    output = []
    for c in list:
        if isNumber(c) == True:
            c = "9"
            output.append(c)
        elif c == " ":
            c = " "
            output.append(c)
        else:
            c = "A"
            output.append(c)
    return output

output = formatCode(sliced_postcode)
print(output)

formats = [
    ["A", "A", "9", "A",  " ", "9", "A", "A"],  # WC postcode area; EC1–EC4, NW1W, SE1P, SW1 | EC1A 1BB
    ["A", "9", "A",       " ", "9", "A", "A"],  # E1, N1, W1 | W1A 0AX
    ["A", "9",            " ", "9", "A", "A"],  # B, E, G, L, M, N, S, W | M1 1AE, B33 8TH
    ["A", "9", "9",       " ", "9", "A", "A"],
    ["A", "A", "9",       " ", "9", "A", "A"],  # All other postcodes | CR2 6XH, DN55 1PT
    ["A", "A", "9", "9",  " ", "9", "A", "A"]
]


def compareOutputToFormats(code):
    sliced_code = []
    print(sliced_code)
    sliced_code[:] = code
    print(sliced_code)
    formatted_code = formatCode(sliced_code)
    print(formatted_code)
    for f in formats:
        if all(x == y for x, y in zip(f, formatted_code)): # https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
            print(f"Postcode matches format {f}")
            return True
        else:
            print("Postcode not valid")

#compareOutputToFormats(sample_postcode)
compareOutputToFormats("BC4D 5FV")