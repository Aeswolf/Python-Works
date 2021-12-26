# function to implement the merge sort algorithm
def merge_sort(item_list):
    """
    :param item_list: the list of items to be sorted
    :return: a list of sorted items
    """

    # base case
    if len(item_list) <= 1:
        return item_list

    else:
        # using variable unpacking and the function split_list to produce two item lists
        left_half_of_list, right_half_of_list = split_list(item_list)

        # variables left and right to hold the repeatedly divided halves of the list
        left = merge_sort(left_half_of_list)

        right = merge_sort(right_half_of_list)

    return merge_list(left, right)


# function for splitting a given list of items into two parts
def split_list(item_list):
    """
    :param item_list: the list of items to be split
    :return: two sub lists from the item_list
    """
    # variable pivot_index to help split the item list given into two parts
    pivot_index = len(item_list) // 2

    # creating the portion of the list whose indexes are less than that of the pivot index
    left_list = item_list[:pivot_index]

    # creating the portion of the list whose indexes are greater than or equal to that of the pivot index
    right_list = item_list[pivot_index:]

    return left_list, right_list


# function to merge the split list together as a single list
def merge_list(left_list, right_list):
    """
    :param left_list: the left portion of the list that was split
    :param right_list: the right portion of the list that was split
    :return: a sorted list obtained from the combination of the left_list and right_list
    """

    # variable sorted_list to hold sorted items
    sorted_list = list()

    # variables left_list_index and right_list_index to help track the items in the left_list and the right_list while
    # merging the left_list and the right_list
    left_list_index, right_list_index = 0, 0

    # while loop to help merge the left_list and right_list if they have the same length
    while left_list_index < len(left_list) and right_list_index < len(right_list):

        # using the if-else statement to rearrange the items by comparison
        if left_list[left_list_index] < right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    # while loop to help merge extra items in the left list when the right list is exhausted
    while left_list_index < len(left_list):
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1

    # while loop to help merge extra items in the right list when the left list is exhausted
    while right_list_index < len(right_list):
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    return sorted_list


print(merge_sort([10, -2, 3, -1, 4, 23, 21, 43, 89, 5, 6, 74, 23]))
