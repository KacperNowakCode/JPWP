import time
from functools import wraps
from datetime import datetime


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000

        log_entry = f"{datetime.now()}: {func.__name__} executed in {elapsed:.2f} ms"
        try:
            with open("profiling_log.txt", "a") as f:
                f.write(log_entry + "\n")
        except IOError as e:
            print(f"Error writing to profiling_log.txt: {e}")


        return {'time': elapsed, 'result': result}

    return wrapper