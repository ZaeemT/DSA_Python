def find_minimum(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

def selection_sort(elements):
    size = len(elements)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j
        
        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == "__main__":
    elements = [78, 12, 15, 8, 2, 61, 53, 23, 27]
    selection_sort(elements)
    print(elements)
    """
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
    """