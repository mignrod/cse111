from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('', '') == '; '
    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    assert make_full_name('Al', 'G') == 'G; Al'
    assert make_full_name('Jason', '') == '; Jason'
    assert make_full_name('', 'Smith') == 'Smith; '

def test_extract_family_name():
    assert extract_family_name('; ') == ''
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('G; Al') == 'G'
    assert extract_family_name('Smith-Jones; Jason') == 'Smith-Jones'

def test_extract_given_name():
    assert extract_given_name('; ') == ''
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('G; Al') == 'Al'
    assert extract_given_name('Smith-Jones; Jason') == 'Jason'
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
