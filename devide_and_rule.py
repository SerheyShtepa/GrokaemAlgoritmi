def suma(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + suma(arr[1:])


def quick_sort(array):
    """быстроя сортировка, розделяй и властвуй, рекурсия"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(hash())