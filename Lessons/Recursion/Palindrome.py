
# function to determine if a word is a palindrome or not
def is_palindrome(word):
    # base cae
    if len(word) == 0 or len(word) == 1:
        return True

    # palindrome condition with recursive call
    if word[len(word) - 1] == word[0]:
        return is_palindrome(word[1:len(word) - 1])

    return False


print(is_palindrome("amani"))