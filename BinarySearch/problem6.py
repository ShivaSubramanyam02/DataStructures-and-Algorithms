def first_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            high = mid - 1  # move left to find earlier occurrence
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            low = mid + 1  
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, key):
    first = first_occurrence(arr, key)
    if first == -1:
        return 0
    last = last_occurrence(arr, key)
    return last - first + 1


arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
key = 5

print("First Occurrence:", first_occurrence(arr, key))
print("Last Occurrence:", last_occurrence(arr, key))
print("Count:", count_occurrences(arr, key))
