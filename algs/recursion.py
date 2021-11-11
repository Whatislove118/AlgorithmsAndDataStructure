
def sum(arr):  # не совсем эффективный подход, так как размерность задачи не уменьшается
    total = 0
    for i in arr:
        total += i
    return total

def recursive_sum(arr):  # эффективнее, так как на каждом шагу мы уменьшааем размерность задачи
    value = arr.pop(0)
    if len(arr) == 0:
        return value
    return value + recursive_sum(arr)

def recursive_count(arr):  # при использовании рекурсии крайне эффективно уменьшать размерность задачи путем перехода к базовому случаю стратегии "Разделяй и властвуй"
    arr.pop(0)
    if len(arr) == 0:
        return 1
    return 1 + recursive_count(arr)

def find_max(arr, max=0):  # упражнение на нахождение максимума с рекурсией
    value = arr.pop(0)
    if value > max:
        max = value
    if len(arr) == 0:
        return max
    max = find_max(arr, max)
    return max


if __name__ == '__main__':
    arr = [2, 4, 100, 5, 2, 1, 11]
    print(sum(arr))
    # print(recursive_sum(arr))
    #print(recursive_count(arr))
    print(find_max(arr))

