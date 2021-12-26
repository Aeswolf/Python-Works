def linear_search(list_of_items, key):
    for index in range(len(list_of_items)):
        if key == list_of_items[index]:
            return index
    else:
        raise Exception(f'{key} does not exist in the list')


def main():
    numbers_list = [number for number in range(-20, 11)]
    print(linear_search(numbers_list, 0))


main()