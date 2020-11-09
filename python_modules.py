# Let's have a look at some built in functions in Python
# import is the keyword we use to call modules from Python libraries
# from random import random  # This gives us access to the functions in the random module and random class
# import math  # This gives us access to the functions in the math module
#
#
# # Because we imported the class and file then we don't need to specify the class name first
# print(random())  # Generates a random float number between 0.0 and 1.0
#
# # Declaring a float and rounding it up and down with imported math methods ceil() and floor()
# num_float = 23.89
# print(" floor() method rounds the figure UP to the nearest integer")
# print(math.floor(num_float))  # Because we only imported the file, we need to specify to use the math class
# print(math.ceil(num_float))
# print(" ceil() method rounds the figure UP to the nearest integer")
# # Using pi
# print(math.pi)
#
# # Task 1
# # Get user input of a float number
# # Check if the number is lower than .50 then round the figure to lower end
# # Check if the number is greater than .51 then round the figure to upper end
#
# user_float = input("Please input a decimal number and watch as it gets rounded to the nearest integer value!  ")
# decimal_index = user_float.find(".")
# if int(user_float[decimal_index+1:decimal_index+2]) >= 5:
#     print(f"That number was closer to its upper bound, so just like magic: {math.ceil(float(user_float))} ")
# elif int(user_float[decimal_index+1:decimal_index+2]) < 5:
#     print(f"That number was closer to its lower bound, so just like magic: {math.floor(float(user_float))} ")

# This helps us to find out system configuration or other system related information
# based on the information provided we can handle the user requests
import os
import math, datetime, sys
# # This will work in linux but not windows
# # working_dir = os.getcwd()
# # print(working_dir)
# # Let's create a method to find out our os
# # print(os.name())  # This is only available in linux and mac
# # Let's count the number of CPU's
# print(os.cpu_count())  # This prints out how many cpus the user has, in this case it prints 8 for my machine
# # datetime module gives us the ability to create, manipulate, and fetch dates and times
# print(datetime.datetime.today())  # This prints out the date and time at execution
# To find out system path
print(sys.path)  # This prints out the full directory path of the current file
# Creating a function that utilises built in functionality to find a users directory and output it to the user


def current_sys_path():
    print("This is your current directory: ")
    return sys.path


print(current_sys_path())
