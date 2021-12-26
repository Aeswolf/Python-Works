
# function to be used for the string reversal
def reverse_string(word):
    """
    :param word: the word or statement to be reversed
    :return: the reversed form of the word augment
    """
    # base case
    if word == "":
        return ""

    return reverse_string(word[1:]) + word[0]


print(reverse_string("God is coming soon"))