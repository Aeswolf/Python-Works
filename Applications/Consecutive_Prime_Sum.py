"""
This is a program that determines the prime number below one million that can expressed as a sum of the
longest consecutive prime numbers.
"""
from math import sqrt


# function to obtain all the prime numbers below a specified value
def prime_numbers(specified_boundary):
    """
    :param specified_boundary: This argument specifies a value below which a group of prime numbers should be generated
    :return: a list of all primes below the specified boundary
    """
    prime_numbers_list = list()

    for number in range(2, specified_boundary):
        if is_prime(number):
            prime_numbers_list.append(number)
    return prime_numbers_list


# function to determine whether a given number is a prime number or not
def is_prime(number):
    """
    :param number: the number whose nature of being a prime number is to be determined
    :return: a boolean indicating the prime nature of the argument
    """
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def longest_consecutive_sequence_counted(array, required_sum):
    for index, value in enumerate(array):
        sum_of_primes = value
        count = 1
        if sum_of_primes == required_sum:
            return count
    
        for next_index in range(index + 1, len(array)):
            sum_of_primes += array[next_index]
            count += 1
            if sum_of_primes == required_sum:
                return count

            elif sum_of_primes > required_sum:
                break
    return -1


def prime_list_generator(prime_numbers_array, prime):
    return [acceptable_prime for acceptable_prime in prime_numbers_array if acceptable_prime <= prime]


prime_number_list = prime_numbers(1000)
usable_prime_numbers_list = [usable_prime_number for usable_prime_number in prime_number_list if usable_prime_number < 970]
longest_count = 0
responsible_prime = 0
for prime_number in usable_prime_numbers_list:
    valid_list = prime_list_generator(prime_number_list, prime_number)
    counter = longest_consecutive_sequence_counted(valid_list, prime_number)
    if counter > longest_count:
        longest_count = counter
        responsible_prime = prime_number
    print(f"{prime_number} => {counter}")

print(f"Longest count : {longest_count} and the responsible prime number is {responsible_prime}")
