import json
import requests
import jsonpath
import pytest

url = "https://reqres.in/api/users"


@pytest.fixture()
def fixture_code():
    global file
    file = open('C:\\Soumyaranjan_Personal\\Study\\API_Testing\\CreateUser.json', 'r')
    print("This is the start of Pytest\n")
    yield
    print("This is the End of Pytest")


# @pytest.mark.skip("This is not valid for current build")
@pytest.mark.Sanity
def test_create_newUser(fixture_code):
    # Read Input json file
    json_input = file.read()
    request_json = json.loads(json_input)
    # make POST Request with json input body
    response = requests.post(url, request_json)
    assert response.status_code == 201


@pytest.mark.Smoke
def test_create_otherUser(fixture_code):
    json_input = file.read()
    request_json = json.loads(json_input)
    # make POST Request with json input body
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    #Pick Id using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
