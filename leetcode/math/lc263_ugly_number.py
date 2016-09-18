"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not
ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""


def is_ugly_number(number):
    """
    Returns True if the number is an ugly number.
    :param number: the number
    :return: True or False
    """
    if number <= 0:
        return False
    if number == 1:
        return True

    primes = {2, 3, 5}
    # keep dividing until it reaches 1 or some other number

    while dividable_by_primes(number, primes):
        for prime in primes:
            if number % prime == 0:
                number /= prime
    return number == 1


def dividable_by_primes(number, primes):
    """
    Returns True if number is dividable by at least one of numbers in the list of `primes`
    """
    return any(number % prime == 0 for prime in primes)
