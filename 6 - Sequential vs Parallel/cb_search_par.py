from multiprocessing import Process, Queue


def CB_search_worker(CB_subdata, CB_target, CB_queue, CB_offset):
    for i, value in enumerate(CB_subdata):
        if value == CB_target:
            CB_queue.put(CB_offset + i)
            return
    CB_queue.put(-1)


def CB_parallel_search(CB_data, CB_target, CB_processes=4):
    CB_chunk_size = len(CB_data) // CB_processes
    CB_queue = Queue()
    CB_process_list = []

    for i in range(CB_processes):
        CB_start = i * CB_chunk_size
        CB_end = CB_start + CB_chunk_size

        CB_process = Process(
            target=CB_search_worker,
            args=(
                CB_data[CB_start:CB_end],
                CB_target,
                CB_queue,
                CB_start
            )
        )

        CB_process_list.append(CB_process)
        CB_process.start()

    CB_results = [CB_queue.get() for _ in CB_process_list]

    for CB_process in CB_process_list:
        CB_process.join()

    for CB_result in CB_results:
        if CB_result != -1:
            return CB_result

    return -1