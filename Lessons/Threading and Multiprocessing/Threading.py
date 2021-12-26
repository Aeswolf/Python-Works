# importing Thread and Lock from the threading module in order to be able to create threads and prevent race conditions
from threading import Thread, Lock


# Defining a function to be used as a target for the created threads
def add_one(number, locker):
    for value in range(50):
        with locker:
            number += value


if __name__ == "__main__":

    # Creating a lock variable to handle race condition
    lock = Lock()

    # Creating an empty list to store the individual threads
    list_of_threads = []

    # for loop for creating threads
    for number_of_threads in range(10):
        a_thread = Thread(target=add_one, args=(0, lock))
        list_of_threads.append(a_thread)

    # for loop to start each created thread
    for thread in list_of_threads:
        thread.start()

    # for loop to join each thread after execution
    for thread in list_of_threads:
        thread.join()

