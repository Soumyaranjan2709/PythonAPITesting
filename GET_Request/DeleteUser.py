import requests

# API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)

print(response.status_code)