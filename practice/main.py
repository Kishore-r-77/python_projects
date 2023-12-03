nums = [1, 2, 3, 4, 5]


def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


swap(nums, 0, 1)
print(nums)
