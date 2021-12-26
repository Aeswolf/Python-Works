def is_even(number): return number % 2 == 0


string = "abc"
string_list = [character for character in string if character.isalpha()]
print(string[0:3])
starting_index = 0
terminating_index = 2
paired_list = []
print(string_list)
print(len(string_list))
while terminating_index != len(string) + 2:
    paired_list.append(string[starting_index:terminating_index])
    starting_index = terminating_index
    terminating_index += 2

print(paired_list)

