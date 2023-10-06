from fizz_buzz import checkio
import pytest
def test_fizz_buzz():
   assert checkio(15) == "Fizz Buzz"
   assert checkio(6) == "Fizz"
   assert checkio(10) == "Buzz"
   assert checkio(7) == "7"



