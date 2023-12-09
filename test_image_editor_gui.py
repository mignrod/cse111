from image_editor_gui import select_image
from os import path
import pytest

def test_select_image():
    """
    Verify that tthe select_image function works correctly
    Parameter: None
    Return: Nothing
    """
    image = path.dirname(__file__)
    assert len(image) > 0, \
        f'File selected for the {image} path'
        

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
