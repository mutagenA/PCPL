import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'time: {time.perf_counter() - self.start:.3f}')
        return False

@contextmanager
def cm_timer_2():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f'time: {time.perf_counter() - start:.3f}')

if __name__ == '__main__':
    print('cm_timer_1, sleep(5.5):')
    with cm_timer_1():
        time.sleep(5.5)

    print('cm_timer_2, sleep(5.5):')
    with cm_timer_2():
        time.sleep(5.5)
