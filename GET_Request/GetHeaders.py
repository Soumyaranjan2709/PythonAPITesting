import requests

headerData = {'T1':"First_Header", 'T2':"Second_Header"}
response = requests.get("http://httpbin.org/get", headers=headerData)
print(response.text)