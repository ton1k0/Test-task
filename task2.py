def find_subarray(arr):
    start, end = 0, 0
    left = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            left = i
        elif i == len(arr) - 1 or (arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]) or (
                arr[i] < arr[i - 1] and arr[i] <= arr[i + 1]):
            if i - left > end - start:
                start, end = left, i
            left = i

    return start, end



print(find_subarray([1, 2, 3, 4, 6, 6, 7, 7, 8]))
print(find_subarray([-1, -1, -1, -1, -1, -1, -1, -1, -1]))






