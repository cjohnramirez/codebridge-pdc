import time
import statistics

CLEAN_MS = 10.0
REPEATS = 3

CASES = [10, 100, 1000]


def simulated_clean(clean_ms):
    time.sleep(clean_ms / 1000.0)


def run_sequential(n_rooms):
    t0 = time.perf_counter()
    for _ in range(n_rooms):
        simulated_clean(CLEAN_MS)
    t1 = time.perf_counter()
    return (t1 - t0) * 1000.0