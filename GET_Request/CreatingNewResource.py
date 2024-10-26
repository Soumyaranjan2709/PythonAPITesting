import json
import requests
import jsonpath

url = "https://reqres.in/api/users"

#Read Input json file
file = open('C:\\Soumyaranjan_Personal\\Study\\API Testing\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

#make POST Request with json input body
response = requests.post(url,request_json)
assert response.status_code == 201

#Fetch Header from Response
print(response.headers.get('Content-Type'))

response_json = json.loads(response.text)

id = jsonpath.jsonpath(response_json,'id')
print(id[0])

