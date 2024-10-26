import requests
import json
import jsonpath
import pytest

def test_add_new_student():
    global StudentID
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\AddStudent.json', 'r')
    jsonRequest = json.loads(f.read())
    response = requests.post(BaseUrl, jsonRequest)
    print(response.text)
    StudentID = jsonpath.jsonpath(response.json(), 'id')
    print(StudentID[0])

def test_get_details():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(StudentID[0])
    jsonResponse = requests.get(API_URL)
    print(jsonResponse.text)




