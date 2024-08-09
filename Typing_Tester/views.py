from Typing_Tester.score_calculator import TypingTestCalculator
from Typing_Tester.report_generator import TypingTestReport
from Typing_Tester.random_word_fetcher import RandomWordFetcher
from Typing_Tester.word import WordDetail
import time
import json


def start_test(start_response, request_body):
    start_time = time.time()
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    start_response(status, headers)
    data = json.loads(request_body)
    api_key = data['api_key']
    word_fetcher = RandomWordFetcher(api_key)
    word = word_fetcher.fetch_word().to_dict()
    response = {'word_to_type': word, 'start_time': start_time}

    return [json.dumps(response, indent=5)]

def end_test(start_response, request_body):
    end_time = time.time()
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    start_response(status, headers)
    data = json.loads(request_body)
    start_time = float(data['start_time'])
    word_to_type = WordDetail.from_json(data['word_to_type'])
    user_typed_word = data['typed_word']
    back_space = int(data['back_spaces_used'])
    score_calculator = TypingTestCalculator()
    time_taken = end_time-start_time
    typing_test_result = score_calculator.compute_total_score(
        str(time_taken),
        user_typed_word,
        word_to_type,
        back_space,
     )
    report_generator = TypingTestReport()
    report = report_generator.generate_report(typing_test_result)

    return [json.dumps(report, indent=5)]


def notfound(start_response):
    status = '404 Notfound'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    response = b'Not Found'

    return [response]

