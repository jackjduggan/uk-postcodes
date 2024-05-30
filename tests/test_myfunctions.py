from postcodelib import myfunctions

valid_codes = [
    "WC1A 1BB",  # Format: ["A", "A", "9", "A",  " ", "9", "A", "A"]
    "EC2N 2DB",
    "SW1A 1AA",
    "W1A 1AA",  # Format: ["A", "9", "A", " ", "9", "A", "A"]
    "N1C 4AB",
    "E1W 3EA",
    "B1 1AA",  # Format: ["A", "9", " ", "9", "A", "A"]
    "M1 1AE",
    "N1 7GU",
    "W12 7RJ",  # Format: ["A", "9", "9", " ", "9", "A", "A"]
    "M60 1NW",
    "B23 6SN",
    "CR2 6XH",  # Format: ["A", "A", "9", " ", "9", "A", "A"]
    "DN55 1PT",
    "RM11 1DU",
    "EC1A 1BB",  # Format: ["A", "A", "9", "9", " ", "9", "A", "A"]
    "SW1W 0NY",
    "NW1W 9QB"
]

invalid_codes = [
    "AAA AA9",
    "9A 9AA"
]

def test_validatePostcode():
    print("===== TESTING VALID POSTCODES =====")
    for code in valid_codes:
        assert myfunctions.validatePostcode(code) == True
        print(f"Postcode: {code} is a valid postcode.")
    print("===== TESTING INVALID POSTCODES =====")
    for code in invalid_codes:
        assert myfunctions.validatePostcode(code) == False
        print(f"Postcode: {code} is an invalid code")

def test_isNumber():
    assert myfunctions.isNumber('A') == False
    assert myfunctions.isNumber('1') == True

def test_sliceCode():
    assert myfunctions.sliceCode('A9 9AA') == ['A', '9', ' ', '9', 'A', 'A']
    assert myfunctions.sliceCode('hello') == ['h', 'e', 'l', 'l', 'o']