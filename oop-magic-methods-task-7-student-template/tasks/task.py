from contextlib import ContextDecorator
import datetime
import time


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        start_str = f"Start: {datetime.datetime.now()} | "
        with open(self.filename, 'a') as f:
            f.write(start_str)

    def __exit__(self, exc_type, exc_value, traceback):
        run_time = time.time() - self.start_time
        run_str = f"Run: {datetime.timedelta(seconds=run_time)} | "
        with open(self.filename, 'a') as f:
            f.write(run_str)
            if exc_type:
                f.write(f"An error occurred: {exc_value}\n")
        return False

@LogFile('my_trace.log')
def some_func():
    try:
        # Code that may raise an exception
        result = 10 / 0
        print(result)  # This won't be executed if an exception occurs
    except ZeroDivisionError as e:
        raise e




if __name__ == '__main__':
    try:
        some_func()
    except ZeroDivisionError:
        pass
