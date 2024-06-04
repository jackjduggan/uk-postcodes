# UK Postcode

Majority of my Python experience thus far had been in the form of standalone script files are jupyter notebooks.\
As such, I followed an article for help creating a Python library (ref1).\

### How It Works
- The main file, `myfunctions.py` contains a function, `validatePostcode` and accompanying helper functions.\
- A user may call this function and pass a string (postcode) as an argument: i.e. `validatePostcode("AB1C 2DE")`.\
- This input is then 'sliced', converting it from a string to a list of characters: `["A", "B", "1", "C", " ", "2", "D", "E"]`.\
- This sliced list is then formatted, with all numbers being represented by "9", all letters by "A", spaces by " ", and anything else by "X": `["A", "A", "9", "A", " ", "9", "A", "A"]`.\
- The formatted code is then compared against a list of valid formats (ref2):

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/40b49bf4-ed0a-4d1e-bc6f-8f816cba3502)
- If the code matches one of the formats, True is returned, else False:

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/ee50070f-6eee-4a1a-9184-a87536062641)
- Additionally, simple tests were implemented with Pytest

![image](https://github.com/jackjduggan/uk-postcodes/assets/74904632/433cdb7e-6d81-43ad-b92a-92a083d361f5)


### Conclusion/References
This could have alternatively been done with Regex, and I likely would have opted for that approach had I scrolled down the wikipedia article a bit more..

ref1: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f \
ref2: https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
