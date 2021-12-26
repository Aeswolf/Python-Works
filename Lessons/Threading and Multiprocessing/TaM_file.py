"""
This file aids in understanding threading and multiprocessing
Threading and Multiprocessing helps to run multiple programs simultaneously and at a fast pace
A process is an instance of a program. An example is running a python interpreter or a web browser
A thread is a unit entity within a process that can be scheduled for execution
A process can possess or spawn multiple threads
To create a process, import Process from the multiprocessing module
Create a list of all the possible processes
Create a variable that stores the number of possible processes based on the number of CPUs on the device(to do this,
import cpu_count from os module
"""
# importing the multiprocessing module
# from multiprocessing import Process
# from os import cpu_count

# Creating the list of the processes

# Creating a variable to store the number of processes based on cpu counts
# number_of_possible_process = cpu_count()

# Steps involved in the creation of a process
# To achieve this, first of all, use a loop to create each process using the Process() function
# The Process() takes two keyword arguments, the first keyword argument is the target argument which refers to the
# function for which the process is being created for and the second keyword argument is the args argument which is
# optional. This optional argument only comes to play if the function passed to the target argument comes with an
# argument.
# Which created process is then added to the processes list.
# A new loop is then created to start each process using the start() function
# Upon completion, the individual processes must be joined together using the join() function


# a function to be passed to the target argument of the Process() function


# for loop to create each process and add to the processes list
#    process = Process(target=perfect_squares)
#    processes_list.append(process
# processes_list[0].start()


# for loop to start each process present in the processes list
#   process.start()


# for loop to join each process upon completion
# for process in processes_list:
# process.join()