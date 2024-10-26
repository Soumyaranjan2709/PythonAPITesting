import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library


def test_add_Multiple_data():
    BaseUrl = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\AddStudent.json', 'r')
    jsonRequest = json.loads(f.read())

    obj = Library.Commom("C:\\Soumyaranjan_Personal\\Study\\API_Testing\\TestCases\\TestData.xlsx","Sheet1")
    col = obj.fetch_column_count()
    row= obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
       updatedJsonRequest = obj.update_request_with_data(i,jsonRequest,keyList)
       response = requests.post(BaseUrl,updatedJsonRequest)
       print(response)