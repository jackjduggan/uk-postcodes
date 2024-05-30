"""
Postcodes are:
- alphanumeric
- variable in length (6-8 chars including space)
- divided into 2 parts separated by space (outward, inward)
"""

formats = [
    ["A", "A", "9", "A",  " ", "9", "A", "A"],  # WC postcode area; EC1–EC4, NW1W, SE1P, SW1 | EC1A 1BB
    ["A", "9", "A",       " ", "9", "A", "A"],  # E1, N1, W1 | W1A 0AX
    ["A", "9",            " ", "9", "A", "A"],  # B, E, G, L, M, N, S, W | M1 1AE, B33 8TH
    ["A", "9", "9",       " ", "9", "A", "A"],
    ["A", "A", "9",       " ", "9", "A", "A"],  # All other postcodes | CR2 6XH, DN55 1PT
    ["A", "A", "9", "9",  " ", "9", "A", "A"]
]

def validatePostcode(code) -> str:
    formatted_code = formatCode(sliceCode(code))
    print(formatted_code)
    for f in formats:
        if all(x == y for x, y in zip(f, formatted_code)): # https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
            print(f"Postcode matches format {f}")
            return True
    return False
        

def isNumber(chr):
    return chr.isdigit()
    
# def checkEachChar(list):
#     for c in list:
#         print(f"Checking: {c}")
#         if isNumber(c) == True:
#             print("True")
#         else:
#             print("False")

def sliceCode(code):
    sliced_code = []
    sliced_code[:] = code
    return sliced_code

def formatCode(list):
    output = []
    for c in list:
        if isNumber(c):
            output.append("9")
        elif c == " ":
            output.append(" ")
        else:
            output.append("A")
    return output