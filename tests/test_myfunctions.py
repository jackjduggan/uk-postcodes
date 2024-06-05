from postcodelib import myfunctions

valid_codes = [
    "WC1A 1bB", # Format: ["A", "A", "9", "A",  " ", "9", "A", "A"]
    "W1A 1AA",  # Format: ["A", "9", "A", " ", "9", "A", "A"]
    "B1 1AA",   # Format: ["A", "9", " ", "9", "A", "A"]
    "W12 7RJ",  # Format: ["A", "9", "9", " ", "9", "A", "A"]
    "Cr2 6XH",  # Format: ["A", "A", "9", " ", "9", "A", "A"]
    "EC1A 1BB", # Format: ["A", "A", "9", "9", " ", "9", "A", "A"]
    "BX5 5AT",  # special cases
    "EC2N 2DB"
]

invalid_codes = [
    "AAA AA9",
    "9A 9AA",
    "AA 9A9AA",
    "A 9A9A",
    "X91X931",
    "XCD7 7VD"
    "hello",
    "WC1A/1bB"
]

def test_validatePostcode():
    for code in valid_codes:
        assert myfunctions.validatePostcode(code) == True
    for code in invalid_codes:
        assert myfunctions.validatePostcode(code) == False

def test_formatCode():
    assert myfunctions.formatCode(["a", "b", "c", "1", "2", "3"]) == ["A", "A", "A", "9", "9", "9"]
    assert myfunctions.formatCode(["a", " ", "c", "1", "?", "3"]) == ["A", " ", "A", "9", "X", "9"]

def test_validateFirstPosition():
    assert myfunctions.validateFirstPosition("ABC") == True     # A is valid first letter
    assert myfunctions.validateFirstPosition("QRS") == False    # Q is invalid first letter

def test_validateSecondPosition():
    assert myfunctions.validateSecondPosition("ABC") == True     # B is valid second letter
    assert myfunctions.validateSecondPosition("IJK") == False    # J is invalid second letter

def test_validateThirdPosition():
    assert myfunctions.validateThirdPosition("A9W") == True     # W is valid third letter
    assert myfunctions.validateThirdPosition("A9Z") == False    # Z is invalid third letter

def test_validateFourthPosition():
    assert myfunctions.validateFourthPosition("AA9W") == True     # W is valid fourth letter
    assert myfunctions.validateFourthPosition("AA9Z") == False    # Z is invalid fourth letter  

def test_validateFinalTwoPositions():
    assert myfunctions.validateFinalTwoPositions("AA AB") == True     # AB valid
    assert myfunctions.validateFinalTwoPositions("AA 7D") == True     # 7D valid
    assert myfunctions.validateFinalTwoPositions("AA CZ") == False    # C is invalid
    assert myfunctions.validateFinalTwoPositions("AA CV") == False    # C and V both invalid

def test_validateSpecialCases():
    assert myfunctions.validateSpecialCases("E20 3HY") == True
    assert myfunctions.validateSpecialCases("NG80 1EH") == True

def test_additionalValidations():
    assert myfunctions.additionalValidations("NG80 1EH") == True
    assert myfunctions.additionalValidations("WC1Z 1bB") == False