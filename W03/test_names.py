from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally","Brown") == 'Brown; Sally'
    assert make_full_name("Sunseehray Alessandra","Tirazona") == 'Tirazona; Sunseehray Alessandra'
    assert make_full_name("A-b","Smith") == 'Smith; A-b'    

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == 'Brown'
    assert extract_family_name("Tirazona; Sunseehray Alessandra") == 'Tirazona'
    assert extract_family_name("Smith; A-b") == 'Smith'  

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == 'Sally'
    assert extract_given_name("Tirazona; Sunseehray Alessandra") == 'Sunseehray Alessandra'
    assert extract_given_name("Smith; A-b") == 'A-b'  

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])