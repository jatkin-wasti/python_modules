# Importing requests to make an api call to web to see if a website is up or not
import requests
from emoji import emojize


# live_response = requests.get("https://www.bbc.co.uk/")  # Getting the response from the website
# print(live_response.status_code)  # Getting the status code from the response
# status_code returns an integer as a response code

# print(live_response.headers)  # Shows dictionary of response headers e.g. date, content type, content length etc.
# print(live_response.content)  # Shows content of the website

# First iteration
# if live_response.status_code == 200:  # the code of 200 means that the website is live
#     print("Mission successful: " + str(live_response.status_code))
#     print(emojize(":thumbs_up:"))
# elif live_response.status_code == 404:  # the code of 404 means that the page was not found
#     print("Oh no. This page is unavailable right now: " + str(live_response.status_code))
# else:
#     print("Oops something went wrong, please try later")


# Second iteration
# def check_response_code(live_response):
#     if live_response.status_code == 200:  # the code of 200 means that the website is live
#         print("Mission successful: " + str(live_response.status_code))
#         print(emojize(":thumbs_up:"))
#     elif live_response.status_code == 404:  # the code of 404 means that the page was not found
#         print("Oh no. This page is unavailable right now: " + str(live_response.status_code))
#     else:
#         print("Oops something went wrong, please try later")
#
#
# check_response_code(requests.get("https://www.bbc.co.uk/"))

# Third iteration
# What does the requests module bring to the table?
# Here we aren't giving conditions but its checking the boolean values which the requests module gets for us
# If the status code is between 200 and 400 then status_code is successful and therefore set to True
# Otherwise it is set to False
def check_response_code(live_response):
    if live_response.status_code:
        print("Mission successful: " + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif live_response.status_code:
        print("Oh no. This, page is unavailable right now: " + str(live_response.status_code))
    else:
        print("Oops something went wrong, please try later")


check_response_code(requests.get("https://www.bbc.co.uk/"))
