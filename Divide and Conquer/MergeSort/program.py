def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        arr = []
        while len(left_half) > 0 and len(right_half) > 0:
            if left_half[0] < right_half[0]:
                arr.append(left_half.pop(0))
            else:
                arr.append(right_half.pop(0))
        arr.extend(left_half)
        arr.extend(right_half)
    return arr


# sample test
# arr = [12, 11, 13, 5, 6, 7]
# print(merge_sort(arr))


# sample usage with user input
# n = int(input())
# arr = [int(x) for x in input().strip().split()]
# print(merge_sort(arr))
