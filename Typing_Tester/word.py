class WordDetail:

    def __init__(self, word: str, definition: str,
                 pronunciation: str):

        self.word = word
        self.definition = definition
        self.pronunciation = pronunciation

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

