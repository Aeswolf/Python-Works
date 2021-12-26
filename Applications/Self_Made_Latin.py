string = input("Enter the string: ")
if ' ' not in string:
    pass
else:
    split_string_by_space = string.split(' ')
    string_without_special_characters = ["".join([letter for letter in word if letter.isalpha()]) for word in split_string_by_space]
    special_characters_string = [letter for word in split_string_by_space for letter in word if not letter.isalnum()]
    print(special_characters_string)
    for main_index, word in enumerate(string_without_special_characters):
        split_word = [letter for letter in word]
        first_letter = split_word[0]
        len_of_word = len(word)
        for index in range(1, len_of_word):
            split_word[index - 1] = split_word[index]
        split_word[len_of_word - 1] = first_letter
        split_word.extend(["a", "y"])
        for special_character in special_characters_string:
            for special_character_index in range(len(split_string_by_space)):
                if special_character in split_string_by_space[special_character_index] and main_index == special_character_index:
                    split_word.extend(special_character)
        string_without_special_characters[main_index] = "".join(split_word)
    print(" ".join(string_without_special_characters))

print(" ".join(x[1:] + x[0] + "ay" for x in string.split(' ')))


