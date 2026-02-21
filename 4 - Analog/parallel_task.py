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