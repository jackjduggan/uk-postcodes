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

def validatePostcode(code: str) -> bool:
    print("--+------------+--")
    print(f"Validating Postcode {code}...")

    formatted_code = formatCode(list(code)) # formats the inputted postcode

    if not additionalValidations(code):
        print("Postcode did not pass validations")
        return False

    # Check format
    for f in formats:
        if all(x == y for x, y in zip(f, formatted_code)):  # checks the input format against the list of valid formats
            print(f"Postcode matches format {f}")           # https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
            print(f"Postcode: {code} is a valid UK Postcode!")
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

def additionalValidations(code :str) -> bool:
    if not validateFirstPosition(code):
        print(f"Invalid character in first position of code: {code}")
        return False
    if not validateSecondPosition(code):
        print(f"Invalid character in second position of code: {code}")
        return False
    if not validateThirdPosition(code):
        print(f"Invalid character in third position of code: {code}")
        return False
    if not validateFourthPosition(code):
        print(f"Invalid character in fourth position of code: {code}")
        return False
    if not validateFinalTwoPositions(code):
        print(f"Invalid character(s) in final two positions of code: {code}")
        return False
    if not validateSpecialCases(code):
        return False
    else:
        print(f"Code: {code} passed additional validation checks.")
        return True

"""
    Validation Functions
"""

def validateFirstPosition(code: str) -> bool:
    invalid_letters = {"Q", "V", "X"}
    if code[0] in invalid_letters:
        return False
    return True

def validateSecondPosition(code: str) -> bool:
    invalid_letters = {"I", "J", "Z"}
    if code[1] in invalid_letters:
        return False
    return True

def validateThirdPosition(code: str) -> bool:
    valid_format = formats[1]
    formatted_code = formatCode(list(code))
    valid_letters = {"A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "P", "S", "T", "U", "V", "W"}

    if formatted_code[:3] == valid_format[:3]:
        if code[2] not in valid_letters:
            return False
    return True

def validateFourthPosition(code: str) -> bool:
    valid_format = formats[0]
    formatted_code = formatCode(list(code))
    valid_letters = {"A", "B", "E", "H", "M", "N", "P", "R", "V", "W", "X", "Y"}

    if formatted_code[:4] == valid_format[:4]:
        if code[3] not in valid_letters:
            return False
    return True

def validateFinalTwoPositions(code: str) -> bool:
    invalid_letters = {"C", "I", "K", "M", "O", "V"}
    for letter in invalid_letters:
        if letter == (code[-1] or code[-2]):
            return False
    return True

def validateSpecialCases(code: str) -> bool:
    regex_pattern = (r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$")
    if not re.match(regex_pattern, code):
        return False
    return True

