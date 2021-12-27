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


def longest_consecutive_sequence(array, required_sum):
    for starter_prime_index in range(len(array)):
        sum_of_primes = array[starter_prime_index]
        count = 1
        for follow_up_primes in range(starter_prime_index + 1, len(array)):
            sum_of_primes += array[follow_up_primes]
            count += 1
            if sum_of_primes == required_sum:
                return count
    return -1


def main():
    prime_numbers_list = primes(100000)
    largest_possible_count = 0
    responsible_prime_number = 0
    for prime in prime_numbers_list:
        print("Current prime :", prime)
        number_counted = longest_consecutive_sequence(prime_numbers_list, prime)
        if largest_possible_count < number_counted:
            largest_possible_count = number_counted
            responsible_prime_number = prime
    print(f"Longest sequence counted is {largest_possible_count} and the prime is {responsible_prime_number}")


main()
