import threading
import time

grades_list = []

print("GWA Calculator \n")
while True:
    grade = input('Enter grades here (enter "stop" if you are finished): ')
    if grade == "stop":
        break
    if grade.isnumeric():
        grades_list.append(int(grade))


partial_sums = []
lock = threading.Lock()


def compute_partial_sum(grades_chunk, thread_id):
    partial = sum(grades_chunk)
    with lock:
        partial_sums.append(partial)
    print(f"[Thread {thread_id}] Partial sum: {partial}")


num_threads = 3
chunk_size = len(grades_list) // num_threads + 1
threads = []

start_execution_time = time.perf_counter()
for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size
    chunk = grades_list[start:end]

    if chunk:
        t = threading.Thread(target=compute_partial_sum, args=(chunk, i))
        threads.append(t)
        t.start()
end_execution_time = time.perf_counter()

for t in threads:
    t.join()

start_printing_time = time.perf_counter()
if len(grades_list) > 0:
    gwa = sum(partial_sums) / len(grades_list)
    print(f"\n[Main] Final GWA: {gwa}")
else:
    print("There is no grade in the list")
end_printing_time = time.perf_counter()

execution_time = end_execution_time - start_execution_time
printing_time = end_printing_time - start_printing_time

print("Execution Time: ", execution_time)
print("Printing Time: ", printing_time)
