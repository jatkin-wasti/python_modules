# use json module to do json encoding and decoding
import json


# Creating a dictionary and storing it into the car_data variable
car_data = {"name": "tesla", "engine": "electric"}
# print(type(car_data))

# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))  # We can see that it has changed type from dict to str
# This is how we can encode from a dictionary and write to a file (w gives write permissions)
with open("new_json_file.json", "w") as jsonfile:  # Writes our data to a json file and aliases the file name
    json.dump(car_data, jsonfile)  # dump all of the data from the car_data variable into the json file
# json.dump() - creates a stream object and accept a file object to write to

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)  # load() copies the data and stores into a variable
    print(type(car))  # We can see that the file has changed back to a dict type
    print(car['name'])
    print(car['engine'])

# getting the value by keys

# Json is used heavily in the industry so reading(encoding), writing(decoding), parsing, and converting data
# are the most commonly utilised options
