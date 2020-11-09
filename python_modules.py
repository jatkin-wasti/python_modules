# Let's have a look at some built in functions in Python
# import is the keyword we use to call modules from Python libraries
# First iteration
import random  # This gives us access to the functions in the random module
import math  # This gives us access to the functions in the math module


print(random.random())  # Generates a random float number between 0.0 and 1.0

# Declaring a float and rounding it up and down with imported math methods ceil() and floor()
num_float = 23.89
print(" floor() method rounds the figure UP to the nearest integer")
print(math.floor(num_float))
print(math.ceil(num_float))
print(" ceil() method rounds the figure UP to the nearest integer")

# Task 1
# Get user input of a float number
# Check if the number is lower than .50 then round the figure to lower end
# Check if the number is greater than .51 then round the figure to upper end

user_float = input("Please input a decimal number and watch as it gets rounded to the nearest integer value!  ")
decimal_index = user_float.find(".")
if int(user_float[decimal_index+1:decimal_index+2]) >= 5:
    print(f"That number was closer to its upper bound, so just like magic: {math.ceil(float(user_float))} ")
elif int(user_float[decimal_index+1:decimal_index+2]) < 5:
    print(f"That number was closer to its lower bound, so just like magic: {math.floor(float(user_float))} ")
