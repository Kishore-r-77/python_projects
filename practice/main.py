nums = [1, 2, 3, 4, 5]


def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def reverse_list(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1


reverse_list(nums)
print(nums)
