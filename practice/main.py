nums = [5, 4, 3, 2, 1]


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    is_asc = arr[start] < arr[end]

    while start <= end:
        mid = int(start + (end - start) / 2)
        if target == arr[mid]:
            return mid
        if is_asc:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


print(binary_search(nums, 1))
