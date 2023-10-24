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
    unique_chars = set(re.findall(r"[a-zA-Z0-9]", password))
    if len(unique_chars) < 3:
        return False
    if "password" in password.lower():
        return False
    if len(password) > 9:
        return True
    if str.isnumeric(password):
        return False
    if len(password) > 6:
        for i in password:
            if str.isdigit(i):
                return True
    return False
