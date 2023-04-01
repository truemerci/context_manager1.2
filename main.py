import time
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("The code did not execute successfully. Error text:", exc_val)
        else:
            print("Code executed successfully in {:.6f} seconds".format(time.time() - self.start))


with Timer() as t:
    print("Hello")


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    except Exception as e:
        print("The code did not execute successfully. Error text:", e)
    else:
        print("Code executed successfully in {:.6f} seconds".format(time.time() - start))


with timer() as f:
    print("Bye")
