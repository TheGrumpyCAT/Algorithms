def binary_search(arr, left, right, k):
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif k > arr[mid]:
            left = mid + 1
        elif k < arr[mid]:
            right = mid - 1
    else:
        return -1


arr = [5, 4, 3, 2, 1]
search_el = 5
print(binary_search(arr, 0, len(arr), search_el))
