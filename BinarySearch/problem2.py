def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return "YES"
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return "NO"



N = 10
A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]   
Q = 3
queries = [23, 50, 91]

for x in queries:
    print(binary_search(A, x))
