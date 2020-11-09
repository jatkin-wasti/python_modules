import requests


response = requests.get("https://api.postcodes.io/postcodes/e147le")
# argument = str(input("Please enter your postcode:  "))
# url_target = response + argument
b = response.json()
# print(b['status'])
# print(b)
# print(b['result']['latitude'])


# research how to convert this data into dictionary
# HINT - python json library/module/method can be used to resolve this


# iterate through the data and print the results
# print longitude and latitude (locations)
# Create a function that returns the longitude and latitude of the given postcode
def check_response_code():
    user_post_code = input("Please enter your post code without spaces e.g. SW1A1AA:  ")
    combined_url = "https://api.postcodes.io/postcodes/" + user_post_code
    live_response = requests.get(combined_url).json()  # Converts the data to dictionary form
    if live_response['status'] == 200:  # Checks if the post code can be found
        print(f"Post code {live_response['result']['postcode']} has been found\n"
              f"Longitude: {live_response['result']['longitude']}\n"
              f"Latitude: {live_response['result']['latitude']}")
    elif live_response['status'] == 404:  # Checks if the API cannot find the post code
        print("Post code not found")
    else:
        print("Oops something went wrong, please try again")


check_response_code()
# This can be used to get random postcodes
# check_response_code(requests.get("https://api.postcodes.io/random/postcodes"))
