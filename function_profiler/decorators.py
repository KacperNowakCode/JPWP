import time
from functools import wraps
from datetime import datetime
# Memory profiling is handled in the GUI, so no need to import memory_usage here
# from memory_profiler import memory_usage

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        # Execute the original function
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000 # Time in milliseconds

        # Log the execution time
        log_entry = f"{datetime.now()}: {func.__name__} executed in {elapsed:.2f} ms"
        #print(log_entry)
        # Append log entry to a file
        try:
            with open("profiling_log.txt", "a") as f:
                f.write(log_entry + "\n")
        except IOError as e:
            print(f"Error writing to profiling_log.txt: {e}")


        # Return a dictionary containing the elapsed time and the original result
        return {'time': elapsed, 'result': result}

    return wrapper