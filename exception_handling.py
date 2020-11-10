# We will have a look at the practical use cases and implementation of try, except, raise, and finally
# We will create a variable to store data from a file using open()
# Iteration 1
try:
    file = open("orders.txt")
except:
    print("File not found")

# Iteration 2
try:
    file = open("orders.txt")
except FileNotFoundError as errmsg:
    print(str(errmsg) + "\nPlease create a file first")
    # If we still wanted them to see the actual exception together with our customised message
    raise  # Outputs the actual error message
finally:  # executes regardless of the above conditions
    print("Hope you had a good experience using our software, we hope you come back soon!")
