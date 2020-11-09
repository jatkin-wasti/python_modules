# Python Modules
## Built in Functions & the Python Library
- Built in Functions help us to accelerate the development of our software
- If we're going to reinvent the wheel there should be a very good reason for doing so
- When importing, the syntax can either be ``` import random``` which will import the entire module, or we can use 
```from random import random``` to import specifically the random function from the random module
- When using the former syntax, you would then need the syntax ```random.random()``` to run the random() method as you 
have to specify the module name before calling objects 
- Whereas, with the latter syntax, you would only need ```random()``` as you've explicitly imported the specified 
functionality
- We can create new methods/functions that use and add on to existing functionality, as can be seen below
### Creating a customised method that utilises built in functions
```
def current_sys_path():
    print("This is your current directory: ")
    return sys.path


print(current_sys_path())
```
### Using installed requests package to test responses to websites
- After installing it with pip (the syntax for this can be found on the pip section down below), we must import it in 
our python file to be able to use it
- We also import emoji's to include them in our response messages
```
import requests
from emoji import emojize
```
- Obtaining the response when trying to access a website (in this case we're using the bbc homepage)
- We then print the https status code that we got as a response
```
live_response = requests.get("https://www.bbc.co.uk/")  # Getting the response from the website
print(live_response.status_code)  # Getting the status code from the response
```
- We then put this functionality into a function that checks the status code and outputs a message to the user 
depending on the code received
```
if live_response.status_code == 200:  # the code of 200 means that the website is live
    print("Mission successful! " + str(live_response.status_code))
    print(emojize((":thumbs_up:")))
elif live_response.status_code == 404:  # the code of 404 means that the page was not found
    print("Oh no. This page could not be found. " + str(live_response.status_code))
else:
    print("Oops something went wrong, please try later")
```
### Putting this code into a function so we can adhere to the DRY principle
```
def check_response_code(live_response):
    if live_response.status_code == 200:  # the code of 200 means that the website is live
        print("Mission successful: " + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif live_response.status_code == 404:  # the code of 404 means that the page was not found
        print("Oh no. This page is unavailable right now: " + str(live_response.status_code))
    else:
        print("Oops something went wrong, please try later")


check_response_code(requests.get("https://www.bbc.co.uk/"))
```
- We then change the function to highlight what the requests module brings to the table
```
def check_response_code(live_response):
    if live_response.status_code:
        print("Mission successful: " + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif !live_response.status_code:
        print("Oh no. This, page is unavailable right now: " + str(live_response.status_code))
    else:
        print("Oops something went wrong, please try later")


check_response_code(requests.get("https://www.bbc.co.uk/"))

```
- Here we aren't giving conditions but its checking the boolean values which the requests module gets for us
- If the status code is between 200 and 400 then status_code is successful and therefore set to True
- Otherwise it is set to False
## What is pip and how do we use it
- Package manager for Python
- Helps us install external packages
- The package we are installing now is called requests
- Syntax is ```pip install name_of_package```
## APIs with Python
- Application Programming Interfacing
- Collection of packages 
![API image](./API_image.png)
## JSON basics
- Java script object notation
- Use cases - browser data
- Data is in key value pairs
- Json encoding from a Dictionary
```
json_string_variable = json.dumps(dictionary_here)
```
- Json decoding into a Dictionary
```
dictionary_variable = json.load(jsonfile)
```
- Handling/creating files with python
```
open("filename.extension", "permission")
```
- The "permission" argument is a placeholder for the letters used to specify the file permissions
- "r" - Read (Default value). Opens file for reading, error occurs if file does not exist
- "a" - Append. Opens file for appending, creates a file if it does not exist
- "w" - Write. Opens file for writing, creates file if it does not exist
- "x" - Create. Creates the specified file, returns an error if the file already exists
- Writing to files
```
open("filename.extension", "w") as alias_name
alias_name.write("stuff_to_write")
alias_name.close()
```
- Reading from files
```
open("filename.extension", "r") as alias_name
first_line = alias_name.readline()
print(first_line)  # This prints out the first line of the file
```
## Exception handling
- Try - Lets you test a block of code for errors
```
try:
    do_this
```
- Except - Lets you handle the error
```
except:
    do_this_if_an_error_is_raised
```
- Raise - Used to raise a exceptions
```
raise TypeOfException("message to output")
```
- Finally - Lets you execute code, regardless of the result of the try and except blocks
```
finally:
    do_this_now
```
- Else - Can be used just like in an if block to execute code if no exceptions were raised
## Tasks
### Task 1
- Get user input of a float number
- Check if the number is lower than .50 then round the figure to lower end
- Check if the number is greater than .51 then round the figure to upper end
### Solution
- Getting the users input and storing it in a variable
```
user_float = input("Please input a decimal number and watch as it gets rounded to the nearest integer value!  ")
```
- Finding the decimal place in the number
```
decimal_index = user_float.find(".")
```
- Checking if the decimal parts are 0.50 or over and rounding up if so
```
if int(user_float[decimal_index+1:decimal_index+2]) >= 5:
    print(f"That number was closer to its upper bound, so just like magic: {math.ceil(float(user_float))} ")
```
- Checking if the decimal parts are less than 0.50 and rounding down if so
```
elif int(user_float[decimal_index+1:decimal_index+2]) < 5:
    print(f"That number was closer to its lower bound, so just like magic: {math.floor(float(user_float))} ")
```
### Task 2
- Obtain user input for their post code
- Use this to get information from the postcodes from the online postcodes API
- Access the information stored in it to output the longitude and latitude values for the given post code
### Solution 
- We need to make requests to the API so we'll import requests
```
import requests
```
- Defining our function, receiving an input from the user and using concatenation to append it to the base url
```
def check_response_code():
    user_post_code = input("Please enter your post code without spaces e.g. SW1A1AA:  ")
    combined_url = "https://api.postcodes.io/postcodes/" + user_post_code
```
- Using the get() function to attempt to retrieve data about the input post code 
```
live_response = requests.get(combined_url).json()
```
- If the status code we get back is 200 then it found the post code and we can output the relevant data
- If the status code is 404 then the post code cannot be found in that API
- The else statement is to catch all other eventualities just in case something different occurs
```        
    if live_response['status'] == 200:
        print(f"Post code {live_response['result']['postcode']} has been found\n"
              f"Longitude: {live_response['result']['longitude']}\n"
              f"Latitude: {live_response['result']['latitude']}")
    elif live_response['status'] == 404:
        print("Post code not found")
    else:
        print("Oops something went wrong, please try again")
```