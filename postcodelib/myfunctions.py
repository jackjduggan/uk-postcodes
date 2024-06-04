import re

"""
This file allows for validation of UK postcodes.
There are a handful of valid postcode formats, which can be seen below.
The validatePostcode function takes a user input (a postcode) and validates its format against the list of valid codes.
    If the postcode is valid, it prints back "Postcode matches format {}" and returns False, else it returns False.
"""
formats = [
    ["A", "A", "9", "A",  " ", "9", "A", "A"],  # WC postcode area; EC1–EC4, NW1W, SE1P, SW1 | EC1A 1BB
    ["A", "9", "A",       " ", "9", "A", "A"],  # E1, N1, W1 | W1A 0AX
    ["A", "9",            " ", "9", "A", "A"],  # B, E, G, L, M, N, S, W | M1 1AE, B33 8TH
    ["A", "9", "9",       " ", "9", "A", "A"],
    ["A", "A", "9",       " ", "9", "A", "A"],  # All other postcodes | CR2 6XH, DN55 1PT
    ["A", "A", "9", "9",  " ", "9", "A", "A"]
]

regex = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

def validatePostcode(code: str) -> bool:
    formatted_code = formatCode(sliceCode(code)) # formats the inputted postcode
    print(formatted_code)
    for f in formats:
        if all(x == y for x, y in zip(f, formatted_code)):  # checks the input format against the list of valid formats
            print(f"Postcode matches format {f}")           # https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
            return True
    return False

def formatCode(list: list) -> list:
    output = []
    for c in list:
        if c.isdigit():     # if number, append "9"
            output.append("9")
        elif c == " ":      # if space, append space
            output.append(" ")
        elif c.isalpha():   # if letter, append "A"
            output.append("A")
        else:               # if anything else, append "X" to invalidate
            output.append("X")
    return output

def sliceCode(code: str) -> list:
    sliced_code = []
    sliced_code[:] = code
    return sliced_code

def validateWithRegex(code: str) -> bool:
    input = code
    print(f"Inputted code: {input}")
    check = re.search(regex, input)
    if check:
        print("Valid Postcode")
        return True
    else:
        print("Invalid Postcode")
        return False
    
# valids
validateWithRegex("EC1A 1BB")
validateWithRegex("W1A 0AX")
validateWithRegex("M1 1AE")
validateWithRegex("B33 8TH")
validateWithRegex("CR2 6XH")
validateWithRegex("DN55 1PT")
# special codes
validateWithRegex("BX2 1LB")
validateWithRegex("E16 1XL")
validateWithRegex("L30 4GB")