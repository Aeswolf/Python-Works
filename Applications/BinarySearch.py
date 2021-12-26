class BinarySearch:
    @staticmethod
    def binary_search(list_of_items, key):
        list_of_items.sort()
        least_index = 0
        largest_index = len(list_of_items) - 1
        while least_index <= largest_index:
            middle_index = (least_index + largest_index) // 2
            if key == list_of_items[middle_index]:
                return middle_index
            elif key > list_of_items[middle_index]:
                least_index = middle_index + 1
            else:
                largest_index = middle_index - 1
        return None  
