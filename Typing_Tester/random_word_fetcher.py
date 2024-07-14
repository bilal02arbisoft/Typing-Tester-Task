import http.client
import json
from .word import WordDetail


class RandomWordFetcher:

    BASE_URL = "wordsapiv1.p.rapidapi.com"
    API_KEY_HEADER = 'x-rapidapi-key'
    HOST_HEADER = 'x-rapidapi-host'
    RANDOM_WORD_ENDPOINT = "/words/?random=true"

    def __init__(self, api_key):

        self.API_KEY = api_key

    def request_api_load_json_data(self):

        connection = http.client.HTTPSConnection(f'{self.BASE_URL}')

        headers = {
            self.API_KEY_HEADER: self.API_KEY,
            self.HOST_HEADER: self.BASE_URL
        }

        connection.request(f'GET', f'{self.RANDOM_WORD_ENDPOINT}',
                           headers=headers)

        fetched_data = connection.getresponse().read()

        return json.loads(fetched_data.decode("utf-8"))

    def fetch_word(self) -> WordDetail:

        # improvement needed
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
