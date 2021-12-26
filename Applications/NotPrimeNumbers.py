def is_prime(value):
    for divisor in range(2, 10000):
        if value % divisor == 0 and value != divisor:
            return False
    return True


def not_prime_number(lower_bound, upper_bound):
    not_prime_number_list = [number for number in range(lower_bound, upper_bound + 1) if not is_prime(number)]
    prime_number_list = [number for number in range(2, 10) if is_prime(number)]
    result_list = list()
    for number in not_prime_number_list:
        count = 0
        string_value = str(number)
        if len(string_value) > 1:
            for index in range(0, len(string_value)):
                for prime_number in prime_number_list:
                    if int(string_value[index]) == prime_number:
                        count += 1
        if count == len(string_value):
            result_list.append(number)
    print(result_list)
    return result_list


not_prime_number(1, 100)