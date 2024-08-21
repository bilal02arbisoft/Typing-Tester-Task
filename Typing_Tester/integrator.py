from Typing_Tester.typingtest import TypingTestManager
from Typing_Tester.score_calculator import TypingTestCalculator
from Typing_Tester.report_generator import TypingTestReport
from Typing_Tester.random_word_fetcher import RandomWordFetcher


def run_typing_test_application():

    try:
        word_fetcher = RandomWordFetcher()
        typing_test_manager = TypingTestManager()
        score_calculator = TypingTestCalculator()
        report_generator = TypingTestReport()
        fetched_word = word_fetcher.fetch_word()
        typing_test_session = typing_test_manager.start_typing_test(fetched_word.word)

        typing_test_result = score_calculator.compute_total_score(
            typing_test_session.time_taken,
            typing_test_session.user_typed_word,
            fetched_word,
            typing_test_session.get_back_spaces_count()
        )

        report = report_generator.generate_report(typing_test_result)
        print(report)

    except Exception as e:
        print(f'{e}')
