import time

from cb_data import CB_generate_data
from cb_sort_seq import CB_merge_sort
from cb_sort_par import CB_parallel_merge_sort
from cb_search_seq import CB_linear_search
from cb_search_par import CB_parallel_search


if __name__ == "__main__":
    CB_sizes = [1000, 100000, 1000000]

    for CB_size in CB_sizes:
        print("\n==============================")
        print("CB DATA SIZE:", CB_size)

        CB_data = CB_generate_data(CB_size)
        CB_target = CB_data[CB_size // 2]

        start = time.time()
        CB_merge_sort(CB_data)
        end = time.time()
        print("Sequential Sort:", end - start)

        start = time.time()
        CB_parallel_merge_sort(CB_data, CB_merge_sort)
        end = time.time()
        print("Parallel Sort:", end - start)

        start = time.time()
        CB_linear_search(CB_data, CB_target)
        end = time.time()
        print("Sequential Search:", end - start)

        start = time.time()
        CB_parallel_search(CB_data, CB_target)
        end = time.time()
        print("Parallel Search:", end - start)