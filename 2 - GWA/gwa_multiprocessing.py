from multiprocessing import Process
import os
import time

def compute_gwa_mp(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Process {os.getpid()}] Calculated GWA: {gwa:.2f}")

if __name__ == "__main__":
    grades = []
    n = int(input("How many subjects? "))

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)

    processes = []

    # ⏱ Start timing
    start_time = time.perf_counter()

    for i in range(3):  # number of processes
        p = Process(target=compute_gwa_mp, args=(grades,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # ⏱ End timing
    end_time = time.perf_counter()

    execution_time_ms = (end_time - start_time) * 1000

    print("All processes completed.")
    print(f"Total Execution Time: {execution_time_ms:.2f} ms")
