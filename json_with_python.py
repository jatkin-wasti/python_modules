# use json module to do json encoding and decoding
import json


# Creating a dictionary and storing it into the car_data variable
car_data = {"name": "tesla", "engine": "electric"}
# print(type(car_data))

# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))  # We can see that it has changed type from dict to str
# This is how we can encode from a dictionary and write to a file (w gives write permissions)
try:
    with open("new_json_file.json", "x") as jsonfile:  # Writes our data to a json file and aliases the file name
        json.dump(car_data, jsonfile)  # dump all of the data from the car_data variable into the json file
        print("File created!")
        jsonfile.close()
except FileExistsError:
    print("Sorry, this file already exists. Try naming it something different.")
# json.dump() - creates a stream object and accept a file object to write to

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)  # load() copies the data and stores into a variable
    print(type(car))  # We can see that the file has changed back to a dict type
    print(car['name'])
    print(car['engine'])

# getting the value by keys

# Json is used heavily in the industry so reading(encoding), writing(decoding), parsing, and converting data
# are the most commonly utilised options

# exception handling
# explain what these all do here, add them to README and include exception handling to check if the
# file is created if not return back the original exception together with customised user friendly message
# try:  # Lets you test a block of code for errors
#     doing_this
# except:  # Lets you handle the error
#     do_this_if_an_error_is_raised
# raise TypeOfException("message to output")  # Used to raise a exceptions
# else:  # Can use this to execute if no exceptions were raised
# finally:  # Lets you execute code, regardless of the result of the try and except blocks
