"""
This is a program that implements the ideology behind the collatz conjecture and uses it to find the number below one
million which has the largest steps in reaching the value one according to the conjecture
Required answer => 837799
"""


# function to count the number of steps(numbers) involved in the reduction of the given to one according to the
# collatz conjecture
def count_element(number):
    # a list to hold all the numbers involved in the reduction
    number_list = list()
    while number not in number_list:
        number_list.append(number)

        if number % 2 == 0:
            number //= 2

        else:
            number = (3 * number) + 1
    print(number_list)

    return len(number_list)


# function to hold the collatz return
def collatz_length(number, memo):
    if number in memo.keys():
        return memo[number]

    memo[number] = count_element(number)

    print(f"{number} => {memo[number]}")

    return memo[number]


m = {}
count = 0
required_number = 0
for _ in range(1, 60):

    value = collatz_length(_, m)
    if count < value:
        count = value
        required_number = _
    print(f"current m => {m}")
print(f"Largest count =>{count} and it corresponds to the number -> {required_number}")