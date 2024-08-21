from Typing_Tester.word import WordDetail


class TypingTestResult:
    """
       A class to represent the result of a typing test.

       Attributes:
           time_score (float): The score based on the time taken to type the word.
           accuracy_score (float): The score based on the accuracy of the typed word.
           total_score (float): The combined total score of the typing test.
           time_taken (str): The time taken by the user to type the word.
           user_typed_word (str): The word that the user typed.
           to_type_word (WordDetail): The original word that the user was supposed to type,
                                      represented as a WordDetail object.
       """
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
        return (
            f'----------Score Report---------\n'
            f'Word: {self.to_type_word.get_word()}\n'
            f'No. of letters: {len(self.to_type_word.get_word())}\n'
            f'User typed: {self.user_typed_word}\n'
            f'Time taken by the user: {self.time_taken} sec\n'
            f'Accuracy Score: {self.accuracy_score:.2f}%\n'
            f'Time Score: {self.time_score:.2f}%\n'
            f'Total Score: {self.total_score:.2f}%\n'
            f'Definition: {self.to_type_word.get_definition()}\n'
            f'Pronunciation: {self.to_type_word.get_pronunciation()}\n'
        )
