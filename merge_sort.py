def merge(array_a, array_b):

    array_c = []

    while len(array_a) != 0 and len(array_b) != 0:
        if array_a[0] < array_b[0]:
            array_c.append(array_a[0])
            array_a.remove(array_a[0])
        else:
            array_c.append(array_b[0])
            array_b.remove(array_b[0])

    if len(array_a) == 0:
        array_c += array_b
    else:
        array_c += array_a

    return array_c

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        middle = len(array) / 2
        array_a = merge_sort(array[:middle])
        array_b = merge_sort(array[middle:])
        return merge(array_a, array_b)

