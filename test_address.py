from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city('525 S Center St, Rexburg, ID 83460') == 'Rexburg'
    assert extract_city('78 Pine St, Avon Park, FL 33825') == 'Avon Park'

def test_extract_state():
    assert extract_state('525 S Center St, Rexburg, ID 83460') == 'ID'
    assert extract_city('78 Pine St, Avon Park, FL 33825') == 'FL'

def test_extract_zipcode():
    assert extract_zipcode('525 S Center St, Rexburg, ID 83460') == '83460'
    assert extract_city('78 Pine St, Avon Park, FL 33825') == '33825'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
