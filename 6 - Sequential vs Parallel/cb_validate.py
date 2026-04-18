from cb_data import CB_generate_data
from cb_sort_seq import CB_merge_sort
from cb_sort_par import CB_parallel_merge_sort
from cb_search_seq import CB_linear_search
from cb_search_par import CB_parallel_search

# For sorting Validation
def CB_is_sorted(CB_data):
    """
    Returns True if the list is sorted in non-decreasing order.
    """
    for i in range(len(CB_data) - 1):
        if CB_data[i] > CB_data[i + 1]:
            return False
    return True


def CB_test_sorting():
    print("\n--- VALIDATING SORTING ---")

    CB_data = CB_generate_data(10_000)

    CB_seq_sorted = CB_merge_sort(CB_data)
    CB_par_sorted = CB_parallel_merge_sort(CB_data, CB_merge_sort)

    print("Sequential Sort Correct:", CB_is_sorted(CB_seq_sorted))
    print("Parallel Sort Correct:", CB_is_sorted(CB_par_sorted))



# For Searching Validation
def CB_test_search():
    print("\n--- VALIDATING SEARCH ---")

    CB_data = CB_generate_data(10_000)
    CB_target = CB_data[5000]
    CB_missing = -999999

    CB_seq_index = CB_linear_search(CB_data, CB_target)
    CB_par_index = CB_parallel_search(CB_data, CB_target)

    print(
        "Sequential Search Found Correct:",
        CB_seq_index != -1 and CB_data[CB_seq_index] == CB_target
    )

    print(
        "Parallel Search Found Correct:",
        CB_par_index != -1 and CB_data[CB_par_index] == CB_target
    )

    print(
        "Sequential Search Not Found:",
        CB_linear_search(CB_data, CB_missing) == -1
    )

    print(
        "Parallel Search Not Found:",
        CB_parallel_search(CB_data, CB_missing) == -1
    )


# Running all tests

if __name__ == "__main__":
    CB_test_sorting()
    CB_test_search()