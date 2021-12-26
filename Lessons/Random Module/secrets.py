import random
from secrets import randbelow
"""
This file helps understand the uses of the secrets module
The secrets module has only three main methods
The secrets module generates values that must be used for passwords, security tokens, account authentications
The disadvantage of the secrets module is the consumption of time in the generation of the values
To use the secrets module, it must first be implemented. Since the secrets module comes with the standard library,
installation is not required
"""


# the randbelow method in this method generates random values beneath the specified upper bound(upper bound is exclusive)
secrets_randbelow_variable = randbelow(8)
print("Randbelow(upper_bound) value ----> ", secrets_randbelow_variable)