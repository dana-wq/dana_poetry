from my_project import fizz_buzz

import pytest
def test_fizz_buzz():
   assert checkio(15) == "Fizz Buzz"
   assert checkio(6) == "Fizz"
   assert checkio(10) == "Buzz"
   assert checkio(7) == "7"
