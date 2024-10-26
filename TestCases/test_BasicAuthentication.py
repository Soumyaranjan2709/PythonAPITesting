import requests
import json
from requests.auth import HTTPBasicAuth

def test_check_auth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('soumya.2799.ranjan@gmail.com', 'Lipuns@123'))
    print(response.text)