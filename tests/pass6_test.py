from my_project import pass6


def test_pass6():
    """
    Password Validation Test

    This module contains unit tests for the password validation implemented in the `pass6` module.

    Usage:
        - Run the tests using Pytest.

    Test Cases:
        - Test case 1: `is_acceptable_password("short")` should return False since the password is too short.
        - Test case 2: `is_acceptable_password("short54")` should return True since the password meets the length requirement.
        - Test case 3: `is_acceptable_password("muchlonger")` should return True since the password meets the length requirement.
        - Test case 4: `is_acceptable_password("ashort")` should return False since the password is too short.
        - Test case 5: `is_acceptable_password("muchlonger5")` should return True since the password meets the length requirement.
        - Test case 6: `is_acceptable_password("sh5")` should return False since the password is too short.
        - Test case 7: `is_acceptable_password("1234567")` should return False since the password lacks variety.
        - Test case 8: `is_acceptable_password("12345678910")` should return True since the password meets the length requirement.
        - Test case 9: `is_acceptable_password("password12345")` should return False since it's a common password.
        - Test case 10: `is_acceptable_password("PASSWORD12345")` should return False since it's a common password.
        - Test case 11: `is_acceptable_password("pass1234word")` should return True since the password meets the complexity requirement.
        - Test case 12: `is_acceptable_password("aaaaaa1")` should return False since it lacks variety.
        - Test case 13: `is_acceptable_password("aaaaaabbbbb")` should return False since it lacks variety.
        - Test case 14: `is_acceptable_password("aaaaaabb1")` should return True since the password meets the complexity requirement.
        - Test case 15: `is_acceptable_password("abc1")` should return False since it's too short.
        - Test case 16: `is_acceptable_password("abbcc12")` should return True since the password meets the complexity requirement.
        - Test case 17: `is_acceptable_password("aaaaaaabbaaaaaaaab")` should return False since it lacks variety.
    """
    assert pass6.is_acceptable_password("short") == False
    assert pass6.is_acceptable_password("short54") == True
    assert pass6.is_acceptable_password("muchlonger") == True
    assert pass6.is_acceptable_password("ashort") == False
    assert pass6.is_acceptable_password("muchlonger5") == True
    assert pass6.is_acceptable_password("sh5") == False
    assert pass6.is_acceptable_password("1234567") == False
    assert pass6.is_acceptable_password("12345678910") == True
    assert pass6.is_acceptable_password("password12345") == False
    assert pass6.is_acceptable_password("PASSWORD12345") == False
    assert pass6.is_acceptable_password("pass1234word") == True
    assert pass6.is_acceptable_password("aaaaaa1") == False
    assert pass6.is_acceptable_password("aaaaaabbbbb") == False
    assert pass6.is_acceptable_password("aaaaaabb1") == True
    assert pass6.is_acceptable_password("abc1") == False
    assert pass6.is_acceptable_password("abbcc12") == True
    assert pass6.is_acceptable_password("aaaaaaabbaaaaaaaab") == False






