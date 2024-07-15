import keyboard
import time


class TypingTestSession:

    def __init__(self, word_typed: str, time_taken: str,
                 back_spaces_used: int):

        self.user_typed_word = word_typed
        self.time_taken = time_taken
        self.back_spaces_count = back_spaces_used

    def __repr__(self) -> str:

        return (f'Typed Word: {self.user_typed_word} \n'
                f'Time Taken: {self.time_taken}\n'
                f'Pronunciation: {self.back_spaces_count}')

    def get_typed_word(self) -> str:

        return self.user_typed_word

    def get_time_taken(self) -> str:

        return self.time_taken

    def get_back_spaces_count(self) -> int:

        return self.back_spaces_count


class TypingInputCapture:

    @staticmethod
    def display_word_on_screen(word):

        print(f'Word to type: {word}')

    @staticmethod
    def wait_for_user_ready() -> None:

        input('Press Enter whenever you are ready to type the word. '
              'After you finish typing Press Enter immediately\n')

    @staticmethod
    def capture_user_input() -> str:

        return input('Start typing ')

    @staticmethod
    def record_start_time() -> float:

        return time.time()

    @staticmethod
    def record_end_time() -> float:

        return time.time()

    @staticmethod
    def compute_time_taken_by_user(start_time, end_time):

        return end_time - start_time


class BackspaceMonitor:

    def __init__(self):

        self.back_space_count = 0

    def increment_back_space_count(self) -> None:

        self.back_space_count += 1

    def reset_back_space_count(self) -> None:

        self.back_space_count = 0

    def get_backspace_count(self) -> int:

        return self.back_space_count

    def monitor_back_space_key(self):

        keyboard.on_press(lambda event: self.increment_back_space_count()
                          if event.name == 'delete' else None)

    @staticmethod
    def stop_monitoring_keys() -> None:

        keyboard.unhook_all()


class TypingTestManager:

    def __init__(self):

        self.input_capture = TypingInputCapture()
        self.monitor_back_space = BackspaceMonitor()
        self.back_space_count = 0

    def start_typing_test(self, word: str) -> TypingTestSession:

        try:

            self.monitor_back_space.reset_back_space_count()
            self.input_capture.display_word_on_screen(word)
            self.monitor_back_space.monitor_back_space_key()
            self.input_capture.wait_for_user_ready()

            start_time = self.input_capture.record_start_time()
            user_typed_word = self.input_capture.capture_user_input()
            end_time = self.input_capture.record_end_time()
            time_taken = self.input_capture.compute_time_taken_by_user(start_time, end_time)

            return TypingTestSession(

                user_typed_word,
                str(round(time_taken, 2)),
                self.monitor_back_space.get_backspace_count()
            )

        except Exception as e:

            raise RuntimeError(f'Error during typing test: {e}')

        finally:

            self.monitor_back_space.stop_monitoring_keys()






