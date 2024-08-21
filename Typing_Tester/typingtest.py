import keyboard
import time


def exception_handler(func):
    """
    Decorator for handling uncaught exceptions in methods.
    Specifically catches KeyError and ValueError, while logging any other exceptions.
    """
    def wrapper(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except (KeyError, ValueError) as e:
            raise e
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    return wrapper


class TypingTestSession:
    """
    Class representing a single typing test session.
    Stores the word typed by the user, the time taken to type it, and the number of backspaces used.
    """

    def __init__(self, word_typed: str, time_taken: str, back_spaces_used: int):
        self.user_typed_word = word_typed
        self.time_taken = time_taken
        self.back_spaces_count = back_spaces_used

    def __repr__(self) -> str:

        return (f'Typed Word: {self.user_typed_word} \n'
                f'Time Taken: {self.time_taken}\n'
                f'Backspaces Used: {self.back_spaces_count}')

    def get_typed_word(self) -> str:
        """
        Returns the word typed by the user during the session.
        """
        return self.user_typed_word

    def get_time_taken(self) -> str:
        """
        Returns the time taken by the user to type the word.
        """
        return self.time_taken

    def get_back_spaces_count(self) -> int:
        """
        Returns the number of backspaces used by the user during the session.
        """
        return self.back_spaces_count


class TypingInputCapture:
    """
    Utility class for capturing typing input from the user, including displaying the word to type,
    recording the time taken, and handling user readiness.
    """

    @staticmethod
    def display_word_on_screen(word):
        print(f'Word to type: {word}')

    @staticmethod
    def wait_for_user_ready() -> None:
        """
        Waits for the user to indicate they are ready by pressing Enter.
        """
        input('Press Enter whenever you are ready to type the word. '
              'After you finish typing Press Enter immediately\n')

    @staticmethod
    def capture_user_input() -> str:

        return input('Start typing: ')

    @staticmethod
    def record_start_time() -> float:
        """
        Records the start time of the typing test.
        """
        return time.time()

    @staticmethod
    def record_end_time() -> float:
        """
        Records the end time of the typing test.
        """
        return time.time()

    @staticmethod
    def compute_time_taken_by_user(start_time, end_time):
        """
        Computes the time taken by the user to type the word.
        """
        return end_time - start_time


class BackspaceMonitor:
    """
    Class responsible for monitoring the backspace key presses during the typing test.
    Tracks how many times the user pressed the backspace key.
    """

    def __init__(self):
        self.back_space_count = 0

    def increment_back_space_count(self) -> None:
        """
        Increments the count of backspace key presses.
        """
        self.back_space_count += 1

    def reset_back_space_count(self) -> None:
        """
        Resets the backspace key press count to zero.
        """
        self.back_space_count = 0

    def get_backspace_count(self) -> int:
        """
        Returns the current count of backspace key presses.
        """
        return self.back_space_count

    def monitor_back_space_key(self):
        keyboard.on_press(lambda event: self.increment_back_space_count()
                          if event.name == 'delete' else None)

    @staticmethod
    def stop_monitoring_keys() -> None:
        """
        Stops monitoring keyboard inputs.
        """
        keyboard.unhook_all()


class Step:
    """
    Base class representing a single step in the Chain of Responsibility.
    Each step processes part of the typing test and passes control to the next step.
    """

    def __init__(self, next_step=None):
        self.next_step = next_step

    def execute(self, *args, **kwargs):
        """
        Executes the current step and passes control to the next step in the chain.
        """
        if self.next_step:

            return self.next_step.execute(*args, **kwargs)

        return None


class DisplayWordStep(Step):
    """
    Step responsible for displaying the word to type on the screen.
    """

    def execute(self, manager, word, *args, **kwargs):
        manager.input_capture.display_word_on_screen(word)

        return super().execute(manager, word, *args, **kwargs)


class MonitorBackspaceStep(Step):
    """
    Step responsible for resetting and starting the backspace key monitoring.
    """

    def execute(self, manager, *args, **kwargs):
        manager.monitor_back_space.reset_back_space_count()
        manager.monitor_back_space.monitor_back_space_key()

        return super().execute(manager, *args, **kwargs)


class WaitForUserStep(Step):
    """
    Step responsible for waiting until the user is ready to start typing.
    """

    def execute(self, manager, *args, **kwargs):
        manager.input_capture.wait_for_user_ready()

        return super().execute(manager, *args, **kwargs)


class CaptureTypingStep(Step):
    """
    Step responsible for recording the start and end times of the typing,
    capturing the user's input, and calculating the time taken.
    """

    def execute(self, manager, *args, **kwargs):
        start_time = manager.input_capture.record_start_time()
        user_typed_word = manager.input_capture.capture_user_input()
        end_time = manager.input_capture.record_end_time()
        time_taken = manager.input_capture.compute_time_taken_by_user(start_time, end_time)

        return super().execute(manager, user_typed_word, time_taken, *args, **kwargs)


class CreateSessionStep(Step):
    """
    Final step responsible for creating the TypingTestSession object
    using the captured user input, time taken, and backspace count.
    """

    def execute(self, manager, user_typed_word, time_taken, *args, **kwargs):
        session = TypingTestSession(
            user_typed_word,
            str(round(time_taken, 2)),
            manager.monitor_back_space.get_backspace_count()
        )

        return session


class TypingTestManager:
    """
    Manager class orchestrating the typing test using a chain of responsibility.
    Handles the entire process from displaying the word to creating a TypingTestSession object.
    """

    def __init__(self):
        self.input_capture = TypingInputCapture()
        self.monitor_back_space = BackspaceMonitor()
        self.chain = DisplayWordStep(
            MonitorBackspaceStep(
                WaitForUserStep(
                    CaptureTypingStep(
                        CreateSessionStep()
                    )
                )
            )
        )

    @exception_handler
    def start_typing_test(self, word: str) -> TypingTestSession:
        """
        Starts the typing test, executing each step in the chain and returning the final TypingTestSession object.
        """
        session = self.chain.execute(self, word)

        return session
