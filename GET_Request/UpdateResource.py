import json
import requests
import jsonpath

url = "https://reqres.in/api/users/2"

#Read Input json file
file = open('C:\\Soumyaranjan_Personal\\Study\\API Testing\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

#make POST Request with json input body
response = requests.put(url,request_json)
assert response.status_code == 200

#Fetch Header from Response
print(response.headers.get('Content-Type'))

response_json = json.loads(response.text)
print(response_json)

updatedAt = jsonpath.jsonpath(response_json,'updatedAt')
print(updatedAt[0])

