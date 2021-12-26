"""
This file contains the implementation of the merge sort algorithm
The merge sort algorithm is an algorithm that was developed aid in the sorting of a group of items.
The algorithm first splits a given list into two portions using the middle item. The newly obtained two portions are
also divided into two new portion using the same idea. This process continues until a unitary item is obtained.
For each split list, the algorithm compares the item and arranges the less item before the greater item.
The algorithm then combines each split item until their entire list is recombined with the items being arranged in
ascending order.
The merge sort algorithm is said to employ three basic procedure namely :
+ Division of the given list
+ Comparing the items and sorting them(conquering the algorithm)
+ Joining each item list together to obtain the overall sorted list
 In this file, the merge sort algorithm is implemented using 3 individual function.
 - The first function is the merge_sort function that executes the two other functions
 - The second function is the split function which divides the list into two portions whenever called
 - The third function is the merge function which is used in joining each separate list to obtain the overall sorted
 list
"""


# The merge_sort function that executes the other functions required for achieving the merge sort algorithm
def merge_sort(item_list):

    # Base case for the recursive calls
    if len(item_list) <= 1:
        return item_list
    else:
        # Using variable unpacking to store the right_half and the left_half of the list
        # the right_half of variable stores all the items in the list the come before the middle item
        # the left_half variable stores all items from the middle item to the very last end of the list
        # the split function provides these required halves
        left_half, right_half = split(item_list)

        # Recursively calling the merge_sort function
        left = merge_sort(left_half)

        right = merge_sort(right_half)

    return merge(left, right)


# The split function for the division the list into two portions
def split(item_list):
    # Variable middle_index to store the index of the element occupying the middle value in the list
    middle_index = len(item_list) // 2

    # Variable left to store the elements that come before the element in the middle
    left = item_list[:middle_index]

    # Variable right to store the elements starting from the middle element to the very last element of the list
    right = item_list[middle_index:]

    return left, right


# The merge which compares the item of each separated lists, sorts them and them joins them into a single list
def merge(left, right):
    # An empty list to hold the sorted list
    sorted_list = list()

    # Variable left_index and right_index to keep track of the indices of the left and right list respectively
    left_index = 0
    right_index = 0

    # while loop to handle the comparison between the left and right list items
    while left_index < len(left) and right_index < len(right):
        # Checking if the item in the left list at a specified index is less than that in the right list at that index
        if left[left_index] < right[right_index]:
            # Appending that item to the sorted_list
            sorted_list.append(left[left_index])
            # Incrementing the left_index
            left_index += 1
        else:
            # Appending that item to the sorted_list
            sorted_list.append(right[right_index])
            # Incrementing the right_index
            right_index += 1

    # While loop to handle the scenario where there are more items in the left list than in the right list
    while left_index < len(left):
        # Appending that item to the sorted_list
        sorted_list.append(left[left_index])
        # Incrementing the left_index
        left_index += 1

    # While loop to handle the scenario where there are more items in the left list than in the right list
    while right_index < len(right):
        # Appending that item to the sorted_list
        sorted_list.append(right[right_index])
        # Incrementing the right_index
        right_index += 1

    return sorted_list


# A method to help verify that a given list has been sorted using the merge sort algorithm
def verify_algorithm(item_list):
    # Returning true for naive sort
    if len(item_list) <= 1:
        return True
    # if not naively sorted, compare each consecutive terms of the list to ensure each item has been correctly sorted
    return item_list[0] < item_list[1] and verify_algorithm(item_list[1:])


a_list = [10, -1, 40, 2, -14, 29, 100, 5, 5, 10, -1, -14, 2, 9]
print(merge_sort(a_list))
print(verify_algorithm(a_list))
print(verify_algorithm(merge_sort(a_list)))