
from my_project import fizz_buzz
import pytest
def test_fizz_buzz():
    """
FizzBuzz Test

This module contains unit tests for the FizzBuzz implementation in the `fizz_buzz` module.

Usage:
    - Ensure that the `fizz_buzz` module is imported from the `my_project` package.
    - Run the tests using  Pytest.

Test Cases:
    - Test case 1: `checkio(15)` should return "Fizz Buzz" since 15 is divisible by both 3 and 5.
    - Test case 2: `checkio(6)` should return "Fizz" since 6 is divisible by 3.
    - Test case 3: `checkio(10)` should return "Buzz" since 10 is divisible by 5.
    - Test case 4: `checkio(7)` should return "7" since 7 is neither divisible by 3 nor 5.

""" 
   assert fizz_buzz.checkio(15) == "Fizz Buzz"
   assert fizz_buzz.checkio(6) == "Fizz"
   assert fizz_buzz.checkio(10) == "Buzz"
   assert fizz_buzz.checkio(7) == "7"



