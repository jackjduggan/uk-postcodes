# UK Postcode

Majority of my Python experience thus far had been in the form of standalone script files are jupyter notebooks.\
As such, I followed the below article for help creating a Python library.\
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

How it works:

The main file, `myfunctions.py` contains a function, `validatePostcode` and accompanying helper functions.\
A user may call this function and pass a string (postcode) as an argument: i.e. `validatePostcode("AB1C 2DE")`.\
This input is then 'sliced', converting it from a string to a list of characters: `["A", "B", "1", "C", " ", "2", "D", "E"]`.\
This sliced list is then formatted, with all numbers being represented by "9", all letters by "A", spaces by " ", and anything else by "X": `["A", "A", "9", "A", " ", "9", "A", "A"]`.\
The formatted code is then compared against a list of valid formats:
[insert image]
If the code matches one of the formats, True is returned, else False.