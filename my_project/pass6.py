"""
Module to check the acceptability of passwords.
"""
import re
def is_acceptable_password(password: str) -> bool:
    """
    Check if the password is acceptable based on certain criteria.
    Criteria:
    - At least three unique characters (alphanumeric).
    - Not containing the word 'password'.
    - If length is greater than 9, it's acceptable.
    - If it's not entirely numeric.
    - If length is greater than 6 and contains at least one digit.
    """
    unique_chars = set(re.findall(r'[a-zA-Z0-9]', password))
    if len(unique_chars) < 3 or "password" in password.lower():
        return False
    if len(password) > 9 or str.isnumeric(password):
        return True
    if len(password) > 6 and any(char.isdigit() for char in password):
        return True
    return False
