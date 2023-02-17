from address import extract_city, \
    extract_state, extract_zipcode
import pytest

# 525 S Center St, Rexburg, ID 83460

def test_extract_city():
    assert extract_city('525 S Center St, Rexburg, ID 83460') == 'Rexburg'

def test_extract_state():
    assert extract_state('525 S Center St, Rexburg, ID 83460') == 'ID'

def test_extract_zipcode():
    assert extract_zipcode('525 S Center St, Rexburg, ID 83460') == '83460'
 

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])