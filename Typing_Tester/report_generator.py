from Typing_Tester.typing_test_result import TypingTestResult


class TypingTestReport:

    @staticmethod
    def generate_report(score_result: TypingTestResult):

        return repr(score_result)
