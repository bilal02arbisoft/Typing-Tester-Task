import http.client
import json
import os
from http import HTTPStatus

from Typing_Tester.word import WordDetail


class APIFetchError(Exception):
    """
    Exception raised for errors in the API fetching process.
    """

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


def error_handler(func):
    """
    Decorator for handling expected and unexpected exceptions.
    Catches APIFetchError, HTTPException, JSONDecodeError, KeyError, ValueError,
    and any other exceptions.
    """

    def wrapper(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except APIFetchError as e:
            print(f"API Fetch Error: {e}")
            raise e
        except (http.client.HTTPException, json.JSONDecodeError) as e:
            print(f"HTTP or JSON Error: {e}")
            raise APIFetchError(f"Error Fetching Data: {e}")
        except (KeyError, ValueError) as e:
            print(f"Data Handling Error: {e}")
            raise e
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return wrapper


def api_request(method: str, endpoint: str, headers: dict) -> dict:
    """
    Utility function for making API requests.
    :param method: HTTP method (e.g., 'GET', 'POST')
    :param endpoint: API endpoint to call
    :param headers: Dictionary of headers to include in the request
    :return: Parsed JSON response
    :raises APIFetchError: If the API call fails or the response is not JSON
    """
    connection = http.client.HTTPSConnection(headers['api-host'])
    connection.request(method, endpoint, headers=headers)
    response = connection.getresponse()

    if response.status != HTTPStatus.OK:
        raise APIFetchError(f'API request failed with status code {response.status}',
                            response.status)

    try:
        fetched_data = response.read()

        return json.loads(fetched_data.decode('utf-8'))
    except (http.client.HTTPException, json.JSONDecodeError) as e:
        raise APIFetchError(f"Error fetching data: {e}")


class RandomWordFetcher:
    RANDOM_WORD_ENDPOINT = os.getenv('WORDS_ENDPOINT')

    def __init__(self):
        self.API_KEY = os.getenv('WORDS_API_KEY')
        self.API_HOST = os.getenv('WORDS_API_HOST')
        self.HEADERS = {
            os.getenv('API_KEY_HEADER'): self.API_KEY,
            os.getenv('HOST_HEADER'): self.API_HOST
        }

    @error_handler
    def fetch_word(self) -> WordDetail:
        """
        Fetches a random word, its definition, and pronunciation from the API.
        Returns a WordDetail object.
        """
        random_word_data = api_request('GET', self.RANDOM_WORD_ENDPOINT, self.HEADERS)
        random_word = random_word_data.get('word', 'Unknown')
        definition = 'Not Found'
        if 'results' in random_word_data and random_word_data['results']:
            definition = random_word_data['results'][0].get('definition', 'Not Found')
        pronunciation = self.extract_pronunciation(random_word_data)

        return WordDetail(random_word, definition, pronunciation)

    @error_handler
    def extract_pronunciation(self, data: dict) -> str:
        """
        Extracts the pronunciation from the API response data.
        Handles both dict and str types for pronunciation data.
        """
        pronunciation_data = data.get('pronunciation', 'Not Found')

        if isinstance(pronunciation_data, dict):

            return pronunciation_data.get('all', 'Not Found')

        return pronunciation_data
