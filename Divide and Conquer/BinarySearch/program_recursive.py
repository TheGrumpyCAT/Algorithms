def binary_search(arr, search_el):
    if len(arr) > 0:
        mid = len(arr) // 2
        mid_el = arr[mid]
        if mid_el == search_el:
            return mid
        elif search_el > mid_el:
            return binary_search(arr[:mid], search_el)
        elif search_el < mid_el:
            return binary_search(arr[mid + 1:], search_el)
    else:
        return -1


arr = [5, 4, 3, 2, 1]
search_el = 5
ans = binary_search(arr, search_el)
print(ans)
