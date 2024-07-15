
from .typingtest import TypingTestManager
from .score_calculator import TypingTestCalculator
from .report_generator import TypingTestReport
from .random_word_fetcher import RandomWordFetcher


def run_typing_test_application(api_key: str):

    try:
        # Initialize the necessary components
        word_fetcher = RandomWordFetcher(api_key)
        typing_test_manager = TypingTestManager()
        score_calculator = TypingTestCalculator()
        report_generator = TypingTestReport()

        # Fetch a random word
        fetched_word = word_fetcher.fetch_word()

        # Start the typing test
        typing_test_session = typing_test_manager.start_typing_test(fetched_word.word)

        # Calculate the score
        typing_test_result = score_calculator.compute_total_score(
            typing_test_session.time_taken,
            typing_test_session.user_typed_word,
            fetched_word,
            typing_test_session.get_back_spaces_count()
        )

        # Generate and display the report
        report = report_generator.generate_report(typing_test_result)
        print(report)

    except Exception as e:

        print(f'{e}')

