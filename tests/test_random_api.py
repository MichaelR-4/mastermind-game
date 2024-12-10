import pytest
from requests.exceptions import HTTPError
from utils.random_number_api import get_random_combination

# injecting the mocker fixtures into test function
@pytest.mark.usefixtures("mocker")
@pytest.mark.parametrize("difficulty_level, expected_result", [("easy", [0,3,5,7]), ("medium", [4,5,6,7,0,1]), ("hard", [1,2,0,4,5,3,6,7])])

def test_api_call (mocker, difficulty_level, expected_result):
  # create mock object to mock requests.get function 
  mock_response = mocker.patch("utils.random_number_api.requests.get")
  mock_response.return_value.status_code = 200
  # simulate text response from the random number generator api
  mock_response.return_value.text = "\n".join(str(num) for num in expected_result)
  #api call trigger 
  result = get_random_combination(difficulty_level)
  assert result == expected_result

@pytest.mark.parametrize("difficulty_level",["easy","medium","hard"])
def test_get_random_combination_invalid_response (mocker, difficulty_level):
  # Mock an invalid response from the API
  mock_response = mocker.patch("utils.random_number_api.requests.get")
  mock_response.return_value.status_code = 200
  mock_response.return_value.text = "not\nnumbers\n"

  with pytest.raises(ValueError):
    get_random_combination(difficulty_level)

@pytest.mark.parametrize("difficulty_level",["easy","medium","hard"])
def test_get_random_combination_api_error (mocker, difficulty_level):
  # Mock an API error response
  mock_response = mocker.patch("utils.random_number_api.requests.get")
  # write custom behavior to raise an HTTPError 
  mock_response.return_value.raise_for_status.side_effect = HTTPError("500 Server Error")

  with pytest.raises(HTTPError, match="500 Server Error"):
     get_random_combination(difficulty_level)
