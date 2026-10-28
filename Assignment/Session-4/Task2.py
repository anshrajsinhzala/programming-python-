"""
2.
Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase,
and replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>
"""

my_string =  " OnePlus Nord-CE 3 "
print(my_string.strip().upper().replace("-",":"))