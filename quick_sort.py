def partition(array, left, right):
    pivot = array[right]
    i = left

    for j in range(left, right):
        if array[j] <= pivot:
            if i != j:
                array[i], array[j] = array[j], array[i]
            i += 1
    if i != right:
        array[i], array[right] = array[right], array[i]
    return i

def quickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quickSort(array, left, p-1)
        quickSort(array, p+1, right)

def main():
    a = [4,7,1,3,9,13,6,5,8,44,1,68,36]
    quickSort(a,0,len(a)-1)
    print a

if __name__ == '__main__':
    main()