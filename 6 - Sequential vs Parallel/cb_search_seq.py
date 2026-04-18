def CB_linear_search(CB_data, CB_target):
    for CB_index, CB_value in enumerate(CB_data):
        if CB_value == CB_target:
            return CB_index
    return -1