import requests
import json
import jsonpath


def test_add_studentData():
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails"
    f  = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\RequestJson.json', 'r')
    jsonRequest = json.loads(f.read())
    response = requests.post(BaseUrl,jsonRequest)
    print(response.text)

def test_update_studentData():
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails/10414107"
    f  = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\RequestJson.json', 'r')
    jsonRequest = json.loads(f.read())
    response = requests.put(BaseUrl,jsonRequest)
    print(response.text)

def test_get_studentData():
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails/10414107"
    GetResponse = requests.get(BaseUrl)
    json_response = json.loads(GetResponse.text)
    ID = jsonpath.jsonpath(json_response, 'data.id')
    assert ID[0] == 10414107

def test_delete_studentData():
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails/10414107"
    DeleteResponse = requests.delete(BaseUrl)
    print(DeleteResponse.text)
