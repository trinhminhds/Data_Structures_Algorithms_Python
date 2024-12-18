def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1

    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index] + [key] + array[index:]


if __name__ == "__main__":
    element_list = [15, 3, 6, 3, 6, 1, 7, 9, 3, 4]
    stream = []
    count = 0
    while (True):
        i = int(input())
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f'Median of {stream}: {stream[(count) // 2]}')
        else:
            i1 = count // 2
            i2 = (count // 2) - 1
            print(f'Median of {stream}: {(stream[i1] + stream[i2]) / 2}')
