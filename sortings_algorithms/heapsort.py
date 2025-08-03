from data_structures.heap import Heap
def heapsort(array):
    heap = Heap()
    for i in range(len(array)):
        heap.insert(array[i])
    for i in range(len(array)):
        array[i] = heap.extract()
    return array
