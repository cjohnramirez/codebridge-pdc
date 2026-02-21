import time
import threading
import statistics

CLEAN_MS = 10.0
TOOLS = 100
REPEATS = 3

CASES = [
    (10, 2),
    (100, 4),
    (1000, 8)
]


def simulated_clean(clean_ms):
    time.sleep(clean_ms / 1000.0)


def chunkify(n_rooms, p):
    rooms = list(range(n_rooms))
    base = n_rooms // p
    rem = n_rooms % p
    chunks = []
    start = 0
    for i in range(p):
        size = base + (1 if i < rem else 0)
        end = start + size
        chunks.append(rooms[start:end])
        start = end
    return chunks

def run_parallel(n_rooms, n_threads):
    sem = threading.Semaphore(TOOLS)
    chunks = chunkify(n_rooms, n_threads)

    def worker(rooms):
        for _ in rooms:
            with sem:
                simulated_clean(CLEAN_MS)

    t0 = time.perf_counter()
    threads = [threading.Thread(target=worker, args=(chunk,)) for chunk in chunks]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    t1 = time.perf_counter()
    return (t1 - t0) * 1000.0

def main():
    print("=== Parallel Benchmark ===")
    print(f"Cleaning time per room: {CLEAN_MS} ms")
    print(f"Tools: {TOOLS} (mutual exclusion)\n")

    for rooms, threads in CASES:
        print(f"Running parallel: {rooms} rooms, {threads} threads")

        times = [run_parallel(rooms, threads) for _ in range(REPEATS)]
        median_ms = statistics.median(times)

        print(f"  Median Parallel Time: {median_ms:.2f} ms\n")


if __name__ == "__main__":
    main()