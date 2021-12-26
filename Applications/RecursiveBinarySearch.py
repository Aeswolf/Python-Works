def recursive_binary_search(list_of_items, key):
    if len(list_of_items) == 0:
        return False
    else:
        middle_index = len(list_of_items) // 2
        if key == list_of_items[middle_index]:
            return True
        else:
            if key < list_of_items[middle_index]:
                return recursive_binary_search(list_of_items[:middle_index], key)
            else:
                return recursive_binary_search(list_of_items[(middle_index + 1):], key)


list_of_numbers = [number for number in range(-300, 300) if number % 2 == 0]
print(recursive_binary_search(list_of_numbers, -400))