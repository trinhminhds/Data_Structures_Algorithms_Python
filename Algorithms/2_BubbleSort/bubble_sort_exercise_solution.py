# you can use this to sort strings too
def bubble_sort(elements, key = None):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            a = elements[j][key]
            b = elements[j + 1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements_name = [
        {'name': 'minh', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'yen', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'y', 'transaction_amount': 200, 'device': 'vi vo'},
        {'name': 'tien', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(elements_name, key = 'transaction_amount')
    print(elements_name)
