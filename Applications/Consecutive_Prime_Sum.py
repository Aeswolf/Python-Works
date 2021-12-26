"""
This is a program that determines the prime below one million that has the longest sum of consecutive prime numbers
"""
from math import sqrt


def is_prime(number):
    square_rooted_value = int(sqrt(number))
    for divisor in range(2, square_rooted_value + 1):
        if number % divisor == 0:
            return False
    return True


def primes(number):
    prime_number_list = []
    for _ in range(2, number):
        if is_prime(_):
            prime_number_list.append(_)
    return prime_number_list


def longest_consecutive_sequence():
   pass



print(longest_consecutive_sequence())