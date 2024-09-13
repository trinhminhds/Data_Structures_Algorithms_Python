def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    element1 = [5, 9, 2, 1, 67, 34, 88, 34]
    element2 = [1, 2, 3, 4, 2]
    element3 = ['mona', 'dhaval', 'aamir', 'tina', 'chang']

    bubble_sort(element1)
    print(element1)
