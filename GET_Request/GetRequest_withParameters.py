import requests
import requests.cookies

param = {'name':"Soumyaranjan", 'email':"Soumyaranjan@gmail.com", 'number':"7682064384"}
response = requests.get("http://httpbin.org/get", params=param)
print(response.text)
