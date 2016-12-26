def parent(node):
    """
    :param node: node of the heap
    :return: the parent of the node
    """
    return node /2

def left(node):
    """
    :param node: node of a heap
    :return: the left child of the node
    """
    return 2*node

def right(node):
    """
    :param node: node of the heap
    :return: the right child of the node
    """
    return 2*node+1

def maxHeapify(array, node, N):

    left_child = left(node)
    right_child = right(node)
    largest = node

    if (left_child <= N) and (array[left_child] > array[largest]):
       largest = left_child

    if right_child <= N and array[right_child] > array[largest]:
        largest = right_child

    if largest != node:
        temp_node = array[largest]
        array[largest] = array[node]
        array[node] = temp_node

        maxHeapify(array, largest, N)

def buildMaxHeap(array, N):
    for i in range(N/2, 0, -1):
        maxHeapify(array, i, N)

def heapSort(array, N):
    array.insert(0, 0)

    buildMaxHeap(array,N)

    while N >= 2:
        temp_node = array[N]
        array[N] = array[1]
        array[1] = temp_node
        N -= 1
        maxHeapify(array, 1, N)
    del array[0]

def main():
    a = [5, 2, 3,7,34,65,12,87,96,21]
    heapSort(a, len(a))
    print a

if __name__ == '__main__':
    main()