from multiprocessing import Process, Queue
from cb_sort_seq import CB_merge


def CB_sort_worker(CB_chunk, CB_queue, CB_sort_func):
    CB_queue.put(CB_sort_func(CB_chunk))


def CB_parallel_merge_sort(CB_data, CB_sort_func, CB_processes=4):
    CB_chunk_size = len(CB_data) // CB_processes
    CB_chunks = [
        CB_data[i:i + CB_chunk_size]
        for i in range(0, len(CB_data), CB_chunk_size)
    ]

    CB_queue = Queue()
    CB_process_list = []

    for CB_chunk in CB_chunks:
        CB_process = Process(
            target=CB_sort_worker,
            args=(CB_chunk, CB_queue, CB_sort_func)
        )
        CB_process_list.append(CB_process)
        CB_process.start()

    CB_sorted_chunks = [CB_queue.get() for _ in CB_process_list]

    for CB_process in CB_process_list:
        CB_process.join()

    CB_sorted_data = CB_sorted_chunks[0]
    for CB_chunk in CB_sorted_chunks[1:]:
        CB_sorted_data = CB_merge(CB_sorted_data, CB_chunk)

    return CB_sorted_data