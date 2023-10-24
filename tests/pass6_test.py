import pytest
from my_project import pass6


def test_pass6():
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
