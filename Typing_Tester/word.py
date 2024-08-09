import json
class WordDetail:

    def __init__(self, word: str, definition: str,
                 pronunciation: str):

        self.word = word
        self.definition = definition
        self.pronunciation = pronunciation

    @classmethod
    def from_json(cls, data):

        return cls(
            word=data['word'],
            definition=data['definition'],
            pronunciation=data['pronunciation']
        )

    def get_word(self) -> str:

        return self.word

    def get_definition(self) -> str:

        return self.definition

    def get_pronunciation(self) -> str:

        return self.pronunciation

    def __repr__(self) -> str:

        return (f'Word: {self.word}\n'
                f'Definition: {self.definition}\n'
                f'Pronunciation: {self.pronunciation}')

    def to_dict(self):

        return {
            'word': self.word,
            'definition': self.definition,
            'pronunciation': self.pronunciation
        }

    def to_json(self):

        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

