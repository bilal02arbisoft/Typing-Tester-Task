import os

from Typing_Tester.integrator import run_typing_test_application

if __name__ == '__main__':
    run_typing_test_application(os.getenv('API_KEY'))
