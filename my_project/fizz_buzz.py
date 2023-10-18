"""
Module to implement the Fizz Buzz game.
"""
def checkio(num: int) -> str:
    """
    Returns 'Fizz' if the input is divisible by 3,
    'Buzz' if divisible by 5, 'Fizz Buzz' if divisible by both,
    and the input number as a string otherwise.
    """
    if num%3 == 0 and num%5 == 0:
        return "Fizz Buzz"
    if num%3 == 0:
        return "Fizz"
    if num%5 == 0 :
        return "Buzz"
    return str(num)
