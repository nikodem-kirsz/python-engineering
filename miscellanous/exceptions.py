import requests

try:
    # Outer try block: Making the API request
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raise an exception if the response status code is not in the 2xx range

    try:
        # Inner try block: Handling JSON parsing and processing
        data = response.json()
        # Perform some processing on the JSON data here

    except ValueError as json_error:
        # Handle JSON parsing errors
        print(f"JSON Parsing Error: {json_error}")
    
except requests.exceptions.RequestException as req_error:
    # Handle API request-related exceptions (e.g., network issues)
    print(f"API Request Error: {req_error}")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"Unexpected Error: {e}")

else:
    # Code to execute when there are no exceptions
    print("API call successful.")

finally:
    # Code to execute regardless of exceptions (e.g., cleanup)
    print("Cleanup or final tasks.")

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is a custom exception.")
except MyCustomError as e:
    print(f"Caught a custom exception: {e}")

class MyCustomError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

try:
    raise MyCustomError("Custom exception with code", code = 42)

except MyCustomError as e:
    print(f"Caught a custom exception: {e}")
    print(f"Exception code: {e.code}")

print("Continueee.....")
