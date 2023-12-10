nums = [1, 2, 5, 9, 22]


def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if target == arr[i] + arr[j]:
                return [i, j]
    return [-1, -1]


print(two_sum(nums, 10))
