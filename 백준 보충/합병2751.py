def quick_sort(node, first, last):
    def partition(first, last):
        pivot = node[last]
        left = first


    for right in range(first, last):
        if node[right] < pivot:
            node[left], node[right] = node[right], node[left]
            left =+ 1
    node[left], node[right] = node[right]. node[left]
    return left
        
if first < last:
    pivot = partition(first, last)
    quick_sort(node, pivot -1)
    quick_sort(node, pivot + 1, last)


