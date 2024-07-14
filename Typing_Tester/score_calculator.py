class TypingTestCalculator:

    @staticmethod
    def wrong_letters_count(user_typed_word, to_type_word) -> int:

        wrong_count = 0

        for i in range(min(len(user_typed_word), len(to_type_word))):

            if user_typed_word[i] != to_type_word[i]:

                wrong_count += 1

        if len(user_typed_word) > len(to_type_word):

            wrong_count += len(user_typed_word) - len(to_type_word)

        elif len(user_typed_word) < len(to_type_word):

            wrong_count += len(to_type_word) - len(user_typed_word)

        return wrong_count

    @staticmethod
    def score_per_letter(user_typed_word, to_type_word):

        return 100 / max(len(user_typed_word), len(to_type_word))

    @staticmethod
    def compute_raw_score(time_taken, user_typed_word):

        return float(time_taken) / (0.4 + (0.28 * (len(user_typed_word) + 1)))

    @staticmethod
    def compute_average_score(time_score, accuracy_score):

        return (time_score + accuracy_score) / 2

    def compute_score_by_letters_count(self, user_typed_word, to_type_word, letters_count):

        return self.score_per_letter(user_typed_word, to_type_word) * letters_count

    def compute_back_space_penalty(self, user_typed_word, to_type_word, back_spaces_count):

        return self.compute_score_by_letters_count(user_typed_word, to_type_word,
                                                   back_spaces_count)

    def compute_misspelled_penalty(self, user_typed_word, to_type_word):

        wrong_letters_count = self.wrong_letters_count(user_typed_word,
                                                       to_type_word)

        return self.compute_score_by_letters_count(user_typed_word, to_type_word,
                                                   wrong_letters_count)

    def compute_negative_score(self, user_typed_word, to_type_word, back_spaces_count):

        negative_score = (self.compute_misspelled_penalty(user_typed_word, to_type_word) +
                          self.compute_back_space_penalty(user_typed_word, to_type_word,
                                                          back_spaces_count))

        return negative_score

    def compute_accuracy_score(self, user_typed_word, to_type_word, back_spaces_count):

        total_penalty_score = self.compute_negative_score(user_typed_word, to_type_word,
                                                          back_spaces_count)

        return (100 - round(total_penalty_score, 2)) if total_penalty_score <= 100 else 0

    @staticmethod
    def process_raw_score(raw_score) -> float:

        if raw_score <= 1:
            return 100

        else:
            if (100 / float(raw_score)) > 0:

                return 100 / float(raw_score)

            else:
                return 0

    def compute_time_score(self, time_taken, user_typed_word) -> float:

        raw_score = self.compute_raw_score(time_taken, user_typed_word)

        return self.process_raw_score(raw_score)

    def compute_total_score(self, time_taken: str, user_typed_word: str,
                            to_type_word: WordDetail, back_spaces_used: int):

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


