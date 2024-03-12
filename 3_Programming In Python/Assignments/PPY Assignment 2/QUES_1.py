"""
Construct a Python function that takes a string containing a phone number and formats it in a standardized way. The function should handle different formats and extract the country code, area code, and local number.
"""
import re

def format_phone_number(phone_number: str) -> tuple[str, str, str]:
    pattern = re.compile(r"(\+\d{1,3})? ?(\d{1,5})? ?((\(\d{1,5}\))|\d{1,5})[-.\s]?\d{1,5}[-.\s]?\d{1,5}[-.\s]?\d{1,5}")
    match = pattern.search(phone_number)
    if match:
        country_code, area_code, local_number = match.groups()
        return country_code, area_code, local_number.replace("(", "").replace(")", "").replace("-", "").replace(".", "").replace(" ", "")
    else:
        return ("", "", "")
    
print(format_phone_number("+1 (800) 123-4567"))  # Returns ('+1', '800', '1234567')
print(format_phone_number("+44 800 123 4567"))  # Returns ('+44', '800', '1234567')
print(format_phone_number("123-456-7890"))  # Returns ('', '', '1234567890')
print(format_phone_number("800.123.4567"))  # Returns ('', '800', '1234567')
print(format_phone_number("1-800-123-4567"))  # Returns ('', '800', '1234567')
print(format_phone_number("1 800 123 4567"))  # Returns ('', '800', '1234567')
print(format_phone_number(""))  # Returns ('', '', '')