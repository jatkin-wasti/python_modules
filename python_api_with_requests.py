# Importing requests to make an api call to web to see if a website is up or not
import requests
from emoji import emojize


live_response = requests.get("https://www.bbc.co.uk/")  # Getting the response from the website
print(live_response.status_code)  # Getting the status code from the response
# status_code returns an integer as a response code
if live_response.status_code == 200:  # the code of 200 means that the website is live
    print("Mission successful! " + str(live_response.status_code))
    print(emojize((":thumbs_up:")))
elif live_response.status_code == 404:  # the code of 404 means that the page was not found
    print("Oh no. This page could not be found. " + str(live_response.status_code))
else:
    print("Oops something went wrong, please try later")
