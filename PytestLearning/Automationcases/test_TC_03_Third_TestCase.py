import pytest


#Testcase code must be written inside a method.
# Method name must be started with test_.
@pytest.fixture(scope="module")
def fixture_code():
    print("This is our fixture code will execute before testcases")
    print("------------------------------------------------------")
    yield
    print("Close DB Connection after the testcases")
    print("------------------------------------------------------")


@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_login_logout_testing(fixture_code):
    print("This is Smoke Test from TC_03")


@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_login_logout_Invalid_Credential(fixture_code):
    print("This is Sanity TestCase from TC_03")

#Print statement output display on console -s
