import requests
import json
import jsonpath
import pytest

def test_oauth_api():

    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type':'password', 'user':'admin','password':'adminpass'}
    Token_response = requests.post(token_url, data)
    print(Token_response.text)
    #x = jsonpath.jsonpath(Token_response.json(),'access_token')

    #d = {'Authorization':'Bearer '+x[0]}
    #print(d)
    API_URL = "https://thetestingworldapi.com/api/StDetails/10414310"
    response = requests.get(API_URL)
    print(response.text)