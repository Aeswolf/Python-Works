def make_diamond(number):
    number_of_spaces = number
    if number % 2 != 0:
        for index in range(0, number):
            number_of_asterisks = ((2 * index) + 1)
            count = 0
            while count < number_of_spaces:
                print(" ", end='')
                count += 1
            number_of_spaces -= 1
            count = 0
            while count < number_of_asterisks:
                print("*", end='')
                count += 1
            print()
    return None


make_diamond(3)
