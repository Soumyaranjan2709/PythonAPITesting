import pytest

#Testcase code must be written inside a method.
# Method name must be started with test_.
# a=101
# @pytest.mark.skip("Skipping as this functionality is not working")
#@pytest.mark.skipif(a>100, reason="Skipping as this functionality is not working")
@pytest.mark.Smoke
def test_tc_001_login_logout_testing():
    print("This is Smoke Test from TC_04")

@pytest.mark.Sanity
def test_tc_003_login_logout_Invalid_Credential():
    print("This is Sanity TestCase from TC_04")

#Print statement output display on console -s
