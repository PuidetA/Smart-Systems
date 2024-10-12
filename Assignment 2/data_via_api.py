import requests # Source: https://www.dataquest.io/blog/python-api-tutorial/
response = requests.get("http://api.open-notify.org/astros") # We fetch the data via REST API.
print(response.json()) # Print out received json data.
"""import json # Same thing but prints out line by line and makes the json more readable.
def printJson(json_file):
    text = json.dumps(json_file, sort_keys=True, indent=4)
    print(text)
printJson(response.json())"""