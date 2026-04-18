def CB_merge_sort(CB_data):
    if len(CB_data) <= 1:
        return CB_data

    CB_mid = len(CB_data) // 2
    CB_left = CB_merge_sort(CB_data[:CB_mid])
    CB_right = CB_merge_sort(CB_data[CB_mid:])

    return CB_merge(CB_left, CB_right)



def CB_merge(CB_left, CB_right):
    CB_result = []
    i = j = 0

    while i < len(CB_left) and j < len(CB_right):
        if CB_left[i] <= CB_right[j]:
            CB_result.append(CB_left[i])
            i += 1
        else:
            CB_result.append(CB_right[j])
            j += 1

    CB_result.extend(CB_left[i:])
    CB_result.extend(CB_right[j:])

    return CB_result
