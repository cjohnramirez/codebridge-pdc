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

def main():
    print("=== Sequential Benchmark ===")
    print(f"Cleaning time per room: {CLEAN_MS} ms\n")

    for rooms in CASES:
        print(f"Running sequential: {rooms} rooms")

        times = [run_sequential(rooms) for _ in range(REPEATS)]
        median_ms = statistics.median(times)

        print(f"  Median Sequential Time: {median_ms:.2f} ms\n")


if __name__ == "__main__":
    main()