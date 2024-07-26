from Typing_Tester.word import WordDetail


class TypingTestResult:

    def __init__(self, time_score: float, accuracy_score: float,
                 total_score: float, time_taken: str, user_typed_word: str,
                 to_type_word: WordDetail):
        self.time_score = time_score
        self.accuracy_score = accuracy_score
        self.total_score = total_score
        self.time_taken = time_taken
        self.user_typed_word = user_typed_word
        self.to_type_word = to_type_word

    def __repr__(self):

        return (f'----------Score Report---------\n'
                f'Word: {self.to_type_word.get_word()}\n'
                f'No. of letters: {len(self.to_type_word.get_word())}\n'
                f'User typed: {self.user_typed_word}\n'
                f'Time taken by the user: {self.time_taken}sec\n'
                f'Accuracy Score: {self.accuracy_score}%\n'
                f'Time Score: {self.time_score}%\n'
                f'Total Score: {self.total_score}%\n'
                f'Definition: {self.to_type_word.get_definition()}\n'
                f'Pronunciation: {self.to_type_word.get_pronunciation()}\n')
