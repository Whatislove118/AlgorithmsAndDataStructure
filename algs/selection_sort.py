

# sort by minimal listen

def find_min(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    result = []
    for i in range(len(arr)):
        smallest_index = find_min(arr)
        result.append(arr.pop(smallest_index))
    return result


if __name__ == '__main__':
    arr = [5, 6, 1, 2, 3]
    print(selection_sort(arr))