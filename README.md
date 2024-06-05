# UK Postcode

Majority of my Python experience thus far had been in the form of standalone script files are jupyter notebooks.\
As such, I followed an article for help creating a Python library (ref1).\

### How It Works
- The main file, `myfunctions.py` contains a function, `validatePostcode` and accompanying helper functions.\
- A user may call this function and pass a string (postcode) as an argument: i.e. `validatePostcode("AB1C 2DE")`.\
- This input is then converted to uppercase (if necessary), and converted from a string to a list of characters: `["A", "B", "1", "C", " ", "2", "D", "E"]`.\
- This list is then formatted, with all numbers being represented by "9", all letters by "A", spaces by " ", and anything else by "X": `["A", "A", "9", "A", " ", "9", "A", "A"]`.\
- The unformatted code is tested against a handful of validations, ensuring invalid characters aren't present and verifying against special cases.
- If it passes these initial validations, the formatted code is then compared against a list of valid formats (ref2):

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/40b49bf4-ed0a-4d1e-bc6f-8f816cba3502)
- If the code matches one of the formats, True is returned, else False:

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/8f95facc-fa5e-4676-a03b-fb6d114249f6)
![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/2840bc6a-8da0-4589-8a4a-38178e5f5348)


- Additionally, simple tests were implemented with Pytest

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/a3d62f3c-1488-4859-8a32-6d9100d029b1)


ref1: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f \
ref2: https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
