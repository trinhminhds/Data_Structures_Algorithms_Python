# you can use this to sort strings too
def merge_sort(elements, key, descending = False):
    size = len(elements)

    if size == 1:
        return elements

    left_list = merge_sort(elements[0:size // 2], key, descending)
    right_list = merge_sort(elements[size // 2:], key, descending)
    sort_list = merge(left_list, right_list, key, descending)

    return sort_list


def merge(left_list, right_list, key, descending = False):
    merged = []
    # if descending == True --> run acs
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:  # len left and right > 0
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))
    # if descending == False --> run desc
    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    # sort age
    sorted_age = merge_sort(elements, key = 'age', descending = False)
    print(sorted_age)

    # sort time hours
    sorted_time = merge_sort(elements, 'time_hours', False)
    print(sorted_time)

    # sort name
    sorted_name = merge_sort(elements, 'name', False)
    print(sorted_name)
