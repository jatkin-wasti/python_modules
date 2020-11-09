# Python Modules
## Built in Functions & the Python Library
- Built in Functions help us to accelerate the development of our software
- If we're going to reinvent the wheel there should be a very good reason for doing so
- When importing, the syntax can either be ``` import random``` which will import the entire module, or we can use 
```from random import random``` to import specifically the random attribute from the random file
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
## What is pip and how do we use it
- Package manager for Python
- Helps us install external packages
- The package we are installing now is called requests
- Syntax is ```pip install name_of_package```
## APIs with Python
- Application Programming Interfacing
- Collection of packages
- ![API image](./API_image.png)
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