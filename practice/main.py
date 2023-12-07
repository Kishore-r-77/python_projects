nums = [22, 33, 44, 10, 8, 6]


def finding_peak_element(arr):
    start = 0
    end = len(arr)
    while start < end:
        mid = int(start + (end - 1) / 2)
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


print(finding_peak_element(nums))
