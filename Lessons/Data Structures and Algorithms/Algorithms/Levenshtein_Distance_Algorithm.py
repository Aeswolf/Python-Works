"""
This program implements the levenshtein algorithm used to determine the minimum number of edit that must be employed to
change one given string into another.
An edit refers to a deletions of a character, an insertion of a character or a character replacement.
An edit is represented by the numerical value 1 in this algorithm
"""


# function to implement the algorithm
def levenshtein_distance(first_word, second_word):
    return levenshtein_helper_function(first_word, second_word, len(first_word), len(second_word))


# helper function to aid with the calculation
def levenshtein_helper_function(first_word, second_word, index_of_first_word, index_of_second_word, memo=None):
    if memo is None:
        memo = dict()

    # Base cases
    if (index_of_first_word, index_of_second_word) in memo.keys():
        return memo[(index_of_first_word, index_of_second_word)]

    elif min(index_of_first_word, index_of_second_word) == 0:
        return max(index_of_first_word, index_of_second_word)

    else:
        first_evaluation = 1 + levenshtein_helper_function(first_word, second_word, index_of_first_word - 1, index_of_second_word, memo)
        second_evaluation = 1 + levenshtein_helper_function(first_word, second_word, index_of_first_word, index_of_second_word - 1, memo)
        third_evaluation = levenshtein_helper_function(first_word, second_word, index_of_first_word - 1, index_of_second_word - 1, memo)

        if first_word[index_of_first_word - 1] != second_word[index_of_second_word - 1]:
            third_evaluation += 1

        memo[(index_of_first_word, index_of_second_word)] = min(first_evaluation, second_evaluation, third_evaluation)

        return memo[(index_of_first_word, index_of_second_word)]


print(levenshtein_distance("Sitting", "Kitten"))


