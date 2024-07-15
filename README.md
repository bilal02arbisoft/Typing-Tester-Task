# Typing-Tester Application

## Introduction
Typing Tester is a Python application designed to help users improve their typing skills.
It presents random words for users to type, tracks their typing speed and accuracy, and generates detailed performance reports.
The application fetches random words from an external API, conducts a typing test, calculates scores, and generates comprehensive performance reports. 
Its modular design ensures that the application is easy to maintain and extend, making it a great tool for both learning and assessment.

## Features
- Fetch random words from an external API.
- Conduct typing tests with user input monitoring.
- Calculate typing test scores based on speed and accuracy.
- Generate detailed reports of typing test results.
- Modular design for easy maintenance and scalability.

## Directory Structure

The application is organized as follows:
```bash
TypingTester-Task/
├── typing_tester/
│   ├── __init__.py              # Initialization script
│   ├── integrator.py            # Integration logic for typing test
│   ├── random_word_fetcher.py   # Module for fetching random words from API
│   ├── report_generator.py      # Module for generating typing test reports
│   ├── score_calculator.py      # Module for calculating typing test scores
│   ├── typing_test_result.py    # Module for handling typing test results
│   ├── typingtest.py            # Module for conducting the typing test
│   ├── word.py                  # Module for word details
├── main.py                      # Main application script
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation file
├── .gitignore                   # Specifies intentionally untracked files to ignore
````
## Dependencies

- Python 3.12.3
- keyboard: For monitoring keyboard events.

## Pre-requisites

- Python 3.12.3 must be installed on your system.
- Internet connection (for fetching random words from the API)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bilal02arbisoft/Typing-Tester-Task.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Typing-Tester-Task
    ```
3. Install dependencies:
   ```bash
    pip3 install -r requirements.txt
    ```
## Detailed Usage
To run the application, use the `main.py` file. Below is example usage :
```sh
sudo python3 main.py 
```
## Sample Outputs:

### Output-1
```bash
----------Score Report---------
Word: ethician
No. of letters: 8
User typed: ethician
Time taken by the user: 1.78sec
Accuracy Score: 100.0%
Time Score: 100%
Total Score: 100.0%
Definition: a philosopher who specializes in ethics
Pronunciation: Not Found
```
#### Output-2
```bash
----------Score Report---------
Word: we'd
No. of letters: 4
User typed: we'd
Time taken by the user: 1.29sec
Accuracy Score: 100.0%
Time Score: 100%
Total Score: 100.0%
Definition: Not found
Pronunciation: wid
```
### Output-3
```bash
----------Score Report---------
Word: giant crab
No. of letters: 10
User typed: giant crac
Time taken by the user: 5.93sec
Accuracy Score: 90.0%
Time Score: 58.68465430016864%
Total Score: 74.34232715008432%
Definition: very large deep-water Japanese crab
Pronunciation: 'dʒaɪənt_kræb
```
## Error Handling
The application includes robust error handling to manage scenarios such as:

- APIFetchError: Raised when there is an issue with fetching data from the API.
- http.client.HTTPException: Raised for HTTP errors during API requests.
- json.JSONDecodeError: Raised for errors in decoding JSON responses.
- ValueError: Raised for invalid input values during the test.
- RuntimeError: Raised for general errors during execution.
Error messages are logged to the console, and the application attempts to handle and recover from errors where possible.

# Code Contributions

## Fork the Repository

1. **Fork the repository** to your GitHub account.
2. Create a new branch for your feature or fix.

## Coding Standards

1. Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines for Python code style.
2. Maintain clarity, readability, and consistency with existing code.

## Testing

1. Write tests to cover your code changes.
2. Ensure all tests pass before submitting a pull request.

## Commit Messages

1. Write clear and descriptive commit messages.
   - Include a summary in the subject line.
   - Provide details in the body if necessary.

## Pull Requests

1. **Create a Pull Request:**
   - Submit a pull request to the main branch of the original repository.
   
2. **Describe Your Changes:**
   - Provide a clear description of your changes in the pull request.
   - Mention any related issues by linking them (#issue_number).


   

    
