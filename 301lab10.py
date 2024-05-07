# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.

from urllib import response
import requests

url = input("Enter the URL: ")
b = input("Choose a method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
print(f"Preparing to send a {b} request to {url}. Confirm? (yes/no)")
if input().lower() != 'yes':
    print("Request canceled.")
    exit()
def interpret_status(code):
    return {200: "Success: Request processed correctly.",
            404: "Error: The requested resource was not found.",
            500: "Error: Internal Server Error."}.get(code, f"Status code {code}: See documentation.")
try:
    response = requests.request(b, url)
    print(interpret_status(response.status_code))
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
except requests.exceptions.RequestException as e:
    print("Failed to make request:", e)



