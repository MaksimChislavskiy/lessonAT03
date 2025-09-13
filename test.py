import pytest
from main import get_random_cat_image

def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'images': 'glkjhjh',
    }
    result = get_random_cat_image()
    assert result == {'images': 'glkjhjh'}

def test_get_random_cat_image_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 404
   result = get_random_cat_image()
   assert result == None