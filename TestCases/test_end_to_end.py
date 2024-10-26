import requests
import json
import jsonpath


def test_Add_new_Student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\RequestJson.json', 'r')
    req_json = json.loads(f.read())
    res = requests.post(API_URL, req_json)
    ID = jsonpath.jsonpath(res.json(), 'id')
    print(ID[0])

    tech_API_URL = "https://thetestingworldapi.com/api/technicalskills"
    f = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\TechDetails.json', 'r')
    req_json = json.loads(f.read())
    req_json['id'] = int(ID[0])
    req_json['st_id'] = ID[0]
    res = requests.post(tech_API_URL, req_json)
    print(res.text)

    Address_API_URL = "https://thetestingworldapi.com/api/addresses"
    f = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\AddressDetails.json', 'r')
    req_json = json.loads(f.read())
    req_json['st_id'] = ID[0]
    res = requests.post(Address_API_URL, req_json)
    print(res.text)

    FinalDetails_API_URL = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(ID[0])
    res = requests.get(FinalDetails_API_URL)
    print(res.text)