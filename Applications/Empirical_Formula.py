"""
This is a program that calculates the empirical formula of a given provided the elements of the compound and their
relative percentages
"""
from math import ceil
global empirical_formula


# function to determine the empirical formula for the compound
def determine_formula(element_dict=None, element_molar_masses=None):
    global empirical_formula
    initial_moles, relative_moles = [], []
    for element_symbol in element_dict.keys():
        initial_moles.append(element_dict[element_symbol] / element_molar_masses[element_symbol])
    least_mole = initial_moles[0]
    for index in range(1, len(initial_moles)):
        if least_mole > initial_moles[index]:
            least_mole = initial_moles[index]
    for index in range(len(initial_moles)) and element_symbol in element_dict.keys():
        relative_moles[index] = ceil(initial_moles[index] / least_mole)
    for element_symbol in element_dict.keys():
        empirical_formula = element_symbol + str(relative_moles[index])
        index += 1
        if index >= len(relative_moles):
            index = 0
            break
    return empirical_formula


print(determine_formula({"C": 40.0, "H": 6.67, "O": 53.3}, {"C": 12.0, "H": 1.00, "O": 16.0}))