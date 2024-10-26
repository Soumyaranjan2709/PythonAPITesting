import requests
import json
import jsonpath
# API URL
url = "https://reqres.in/api/users?page=2"

#Send Get Request
response = requests.get(url)

#Parse Response to JSON Format
json_response = json.loads(response.text)
print(json_response)

pages = jsonpath.jsonpath(json_response,  'per_page')
Page_Number = pages[0]

#Fetch Value using JSON Path
for i in range(0,Page_Number):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])

pages = jsonpath.jsonpath(json_response,  'total_pages')
