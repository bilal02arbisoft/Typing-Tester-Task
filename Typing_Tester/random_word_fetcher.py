import http.client
import json
from .word import WordDetail


class APIFetchError(Exception):
    """
    Exception raised for errors in the API fetching process.
    """
    def __init__(self, message, status_code=None):

        super().__init__(message)
        self.status_code = status_code


class RandomWordFetcher:

    BASE_URL = "wordsapiv1.p.rapidapi.com"
    API_KEY_HEADER = 'x-rapidapi-key'
    HOST_HEADER = 'x-rapidapi-host'
    RANDOM_WORD_ENDPOINT = "/words/?random=true"

    def __init__(self, api_key):

        self.API_KEY = api_key

    def request_api_load_json_data(self):

        try:
            connection = http.client.HTTPSConnection(f'{self.BASE_URL}')
            headers = {
                self.API_KEY_HEADER: self.API_KEY,
                self.HOST_HEADER: self.BASE_URL
            }
            connection.request(f'GET', f'{self.RANDOM_WORD_ENDPOINT}',
                               headers=headers)
            response = connection.getresponse()

            if response.status != 200:

                raise APIFetchError(f'API request failed with status code {response.status}',
                                    response.status)

            fetched_data = response.read()

            return json.loads(fetched_data.decode("utf-8"))

        except (http.client.HTTPException, json.JSONDecodeError) as e:

            raise APIFetchError(f'Error fetching data from API: {e}')

    def fetch_word(self) -> WordDetail:

        try:
            random_word_data = self.request_api_load_json_data()
            random_word = random_word_data['word']
            definition = 'Not found'
            pronunciation = 'Not Found'

            if ('results' in random_word_data and
               len(random_word_data['results']) > 0):

                definition = random_word_data['results'][0].get('definition', 'Not Found')

            if 'pronunciation' in random_word_data:

                pronunciation_data = random_word_data['pronunciation']

                if isinstance(pronunciation_data, dict):

                    pronunciation = pronunciation_data.get('all', 'Not found')

                else:

                    pronunciation = pronunciation_data

            return WordDetail(

                random_word,
                definition,
                pronunciation
            )

        except APIFetchError as e:

            raise APIFetchError(f'Error Fetching Random Word from API: {e}')

        except Exception as e:

            raise ValueError(f'Error occurred : {e}')
