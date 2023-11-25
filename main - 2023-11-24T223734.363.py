import time
import numpy as np

def slow_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

def fast_function():
    return np.sum(np.arange(1000000))

if __name__ == "__main__":
    start_time = time.time()
    result_slow = slow_function()
    end_time = time.time()
    print(f"Slow function result: {result_slow}")
    print(f"Time taken by slow function: {end_time - start_time} seconds")

    start_time = time.time()
    result_fast = fast_function()
    end_time = time.time()
    print(f"Fast function result: {result_fast}")
    print(f"Time taken by fast function: {end_time - start_time} seconds")
