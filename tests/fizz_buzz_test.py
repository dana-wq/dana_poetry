from my_project import fizz_buzz
import pytest
def test_fizz_buzz():
   assert fizz_buzz.checkio(15) == "Fizz Buzz"
   assert fizz_buzz.checkio(6) == "Fizz"
   assert fizz_buzz.checkio(10) == "Buzz"
   assert fizz_buzz.checkio(7) == "7"



