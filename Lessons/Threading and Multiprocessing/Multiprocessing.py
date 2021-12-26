# importing Process from multiprocessing to enable the creation of a process
from multiprocessing import Process, Value, Array, Lock

# importing cpu_count from the os module to determine the number of possible processes that can be created
from os import cpu_count

# importing sleep from the time module to cause a little delay for every execution of the function
from time import sleep


# Creating a function to use as target for the process creation
def add_one(number, numbers, locker):
    for index in range(100):
        sleep(0.05)
        # using a context manager with the lock
        with locker:
            number.value += index
            for index_one in range(len(numbers)):
                numbers[index_one] += 10


if __name__ == "__main__":

    # Creating an empty list into which all the possible processes will be stored
    list_of_processes = list()

    # Creating a value that will be shared by multiple processes
    shared_value = Value('i', 0)

    # Creating an array that will be shared by multiple processes
    shared_array = Array('i', [0, 1, 2, 3, 4, 5])

    # Printing the initial value of the shared value
    print("Initial value of the shared value : ", shared_value.value)
    print("Initial array content : ", shared_array[:])

    # Creating a lock variable to handle a race condition
    lock = Lock()

    # Creating for loop to create each process
    for number_of_times in range(cpu_count()):
        # a_process = Process(target=add_one, args=(shared_value, lock))
        array_process = Process(target=add_one, args=(shared_value, shared_array, lock))
        # list_of_processes.append(a_process)
        list_of_processes.append(array_process)

    # Creating a for loop to start all the created processes
    for process in list_of_processes:
        process.start()

    # Joining each process after it is finished using a for loop
    for process in list_of_processes:
        process.join()

    # Printing the value of the shared value after being edited by the processes
    print("final value of the shared value : ", shared_value.value)
    print("final array content : ", shared_array[:])

