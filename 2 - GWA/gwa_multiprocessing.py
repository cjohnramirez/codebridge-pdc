from multiprocessing import Process
import os

def compute_gwa_mp(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Process {os.getpid()}] Calculated GWA: {gwa:.2f}")

if __name__ == "__main__":
    grades = []
    n = int(input("How many subjects? "))

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)

    # Create multiple processes (each computes GWA independently)
    processes = []

    for i in range(3):  # number of processes (can be changed)
        p = Process(target=compute_gwa_mp, args=(grades,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")
