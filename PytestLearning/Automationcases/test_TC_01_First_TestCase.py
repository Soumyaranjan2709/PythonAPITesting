import pytest

#Testcase code must be written inside a method.
# Method name must be started with test_.

actual_result = "Testing"

# a=101
# @pytest.mark.skip("Skipping as this functionality is not working")
#@pytest.mark.skipif(a>100, reason="Skipping as this functionality is not working")
@pytest.mark.TopPriority
def test_tc_001_login_logout_testing():
    print("This is Smoke Test TC_01")
    assert actual_result != "Testing", "These two value must not be same"

@pytest.mark.TopPriority
def test_tc_003_login_logout_Invalid_Credential():
    print("This is Sanity TC_01")
    print("This is end of testcases.")

#Print statement output display on console -s
