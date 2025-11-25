def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_desc(left)
        merge_sort_desc(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [2, 6, 5, 1, 7, 4, 3]
merge_sort_desc(arr)
print("Sorted in decreasing order:", arr)
