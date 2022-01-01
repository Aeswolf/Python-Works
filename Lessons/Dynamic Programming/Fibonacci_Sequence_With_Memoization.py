"""
This is a program that evaluates the nth term of the fibonacci sequence.
This is an optimized procedure using memoization
"""


# function to determine the nth term of the fibonacci sequence
def fibonacci_sequence(term, memo=None):
    """
    :param term: the required term to be evaluated
    :param memo: a dictionary to store already evaluated terms
    :return: the value occupying the term at hand
    """
    # if the memo has no content(that is if the memo is none) , set it to an empty dictionary
    if memo is None:
        memo = dict()

    # if the term being considered is already present in the dictionary as a key, return the value corresponding to the
    # key
    if term in memo.keys():
        return memo[term]

    # if the term is not present in the memo and is either the first or second term, return one
    if term <= 2:
        if term == 1:
            return 1
        return 2

    # else if the term is not present in the memo and also not the first or second term, evaluate the value and store
    # that as the value of the term as key to the memo
    memo[term] = fibonacci_sequence(term - 1, memo) + fibonacci_sequence(term - 2, memo)

    # return the value evaluated for the term at hand
    return memo[term]


print(fibonacci_sequence(32))