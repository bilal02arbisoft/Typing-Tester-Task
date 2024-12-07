from Typing_Tester.typing_test_result import TypingTestResult
from Typing_Tester.word import WordDetail

BASE_TIME_DIVISOR = 0.4
TIME_MULTIPLIER = 0.28


def error_handler(func):
    """
    Decorator for handling expected and unexpected exceptions.
    Catches ValueError specifically and then any other general exceptions.
    """
    def wrapper(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except ValueError as e:
            raise ValueError(f'Error Occurred in {func.__name__}: {e}')
        except Exception as e:
            raise RuntimeError(f'Unexpected Error Occurred in {func.__name__}: {e}')

    return wrapper


class TypingTestCalculator:

    @staticmethod
    @error_handler
    def wrong_letters_count(user_typed_word, to_type_word) -> int:
        """
        Calculate the number of wrong letters in the user's typed word compared to the target word.
        """
        wrong_count = sum(1 for i in range(min(len(user_typed_word), len(to_type_word)))
                          if user_typed_word[i] != to_type_word[i])
        wrong_count += abs(len(user_typed_word) - len(to_type_word))

        return wrong_count

    @staticmethod
    @error_handler
    def score_per_letter(user_typed_word, to_type_word) -> float:
        """
        Calculate the score per letter, based on the length of the longer word.
        """
        return 100 / max(len(user_typed_word), len(to_type_word))

    @staticmethod
    @error_handler
    def compute_raw_score(time_taken: str, user_typed_word: str) -> float:
        """
        Compute the raw score based on time taken and word length.
        """
        return float(time_taken) / (BASE_TIME_DIVISOR + (TIME_MULTIPLIER * (len(user_typed_word) + 1)))

    @staticmethod
    @error_handler
    def compute_average_score(time_score: float, accuracy_score: float) -> float:
        """
        Compute the average score based on time and accuracy scores.
        """
        return (time_score + accuracy_score) / 2

    @error_handler
    def compute_score_by_letters_count(self, user_typed_word: str,
                                       to_type_word: str, letters_count: int) -> float:
        """
        Compute the score based on the number of letters and the score per letter.
        """
        return self.score_per_letter(user_typed_word, to_type_word) * letters_count

    @error_handler
    def compute_back_space_penalty(self, user_typed_word: str,
                                   to_type_word: str, back_spaces_count: int) -> float:
        """
        Compute the penalty score based on the number of backspaces used.
        """
        return self.compute_score_by_letters_count(user_typed_word, to_type_word, back_spaces_count)

    @error_handler
    def compute_misspelled_penalty(self, user_typed_word: str, to_type_word: str) -> float:
        """
        Compute the penalty score based on the number of misspelled letters.
        """
        wrong_letters_count = self.wrong_letters_count(user_typed_word, to_type_word)

        return self.compute_score_by_letters_count(user_typed_word, to_type_word, wrong_letters_count)

    @error_handler
    def compute_negative_score(self, user_typed_word: str,
                               to_type_word: str, back_spaces_count: int) -> float:
        """
        Compute the total negative score based on misspelled letters and backspaces used.
        """
        negative_score = (self.compute_misspelled_penalty(user_typed_word, to_type_word) +
                          self.compute_back_space_penalty(user_typed_word, to_type_word, back_spaces_count))
        return negative_score

    @error_handler
    def compute_accuracy_score(self, user_typed_word: str,
                               to_type_word: str, back_spaces_count: int) -> float:
        """
        Compute the accuracy score after applying all penalties.
        """
        total_penalty_score = self.compute_negative_score(user_typed_word, to_type_word, back_spaces_count)
        return max(100 - round(total_penalty_score, 2), 0)

    @staticmethod
    @error_handler
    def process_raw_score(raw_score: float) -> float:
        """
        Process the raw score to ensure it's within valid bounds.
        """
        return max(100 / float(raw_score), 0) if raw_score > 1 else 100

    @error_handler
    def compute_time_score(self, time_taken: str, user_typed_word: str) -> float:
        """
        Compute the time score based on the raw score.
        """
        raw_score = self.compute_raw_score(time_taken, user_typed_word)

        return self.process_raw_score(raw_score)

    @error_handler
    def compute_total_score(self, time_taken: str, user_typed_word: str,
                            to_type_word: WordDetail, back_spaces_used: int) -> TypingTestResult:
        """
        Compute the total score, combining time and accuracy scores, and return a TypingTestResult object.
        """
        time_score = self.compute_time_score(time_taken, user_typed_word)
        accuracy_score = self.compute_accuracy_score(user_typed_word, to_type_word.get_word(),
                                                     back_spaces_used)
        total_score = self.compute_average_score(time_score, accuracy_score)

        return TypingTestResult(
            time_score,
            accuracy_score,
            total_score,
            time_taken,
            user_typed_word,
            to_type_word
        )
