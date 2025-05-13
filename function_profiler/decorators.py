import time
from functools import wraps
from datetime import datetime
from memory_profiler import memory_usage

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000
        log_entry = f"{datetime.now()}: {func.__name__} executed in {elapsed:.2f} ms"
        print(log_entry)
        with open("profiling_log.txt", "a") as f:
            f.write(log_entry + "\n")
        return result
    return wrapper

# def measure_memory(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         mem_before = memory_usage()[0]
#         result = func(*args, **kwargs)
#         mem_after = memory_usage()[0]
#         delta = mem_after - mem_before
#         log_entry = f"{datetime.now()}: {func.__name__} memory delta {delta:.2f} MiB"
#         print(log_entry)
#         with open("profiling_log.txt", "a") as f:
#             f.write(log_entry + "\n")
#         return result
#     return wrapper