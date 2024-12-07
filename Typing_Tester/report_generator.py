from Typing_Tester.typing_test_result import TypingTestResult


class TypingTestReport:
    """
        Class responsible for generating reports based on the typing test results.
    """
    @staticmethod
    def generate_report(score_result: TypingTestResult):

        return repr(score_result)
