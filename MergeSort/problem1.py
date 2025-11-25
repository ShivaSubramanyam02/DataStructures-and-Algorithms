def mergesort(arr):
    if len(arr) > 1:
        # 1. Split the array into 2 halves
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # 2. Recursively call mergesort on both halves
        mergesort(left_arr)
        mergesort(right_arr)

        # 3. Merge step (combine left and right into sorted order)
        i = 0  # pointer for left_arr
        j = 0  # pointer for right_arr
        k = 0  # pointer for main arr

        # compare elements from both halves and put smaller one into arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1   # move pointer in left_arr
            else:
                arr[k] = right_arr[j]
                j += 1   # move pointer in right_arr
            k += 1       # move pointer in main arr

        # 4. Copy remaining elements of left_arr if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # 5. Copy remaining elements of right_arr if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Example run
arr = [2, 6, 5, 1, 7, 4, 3]
mergesort(arr)
print("Sorted array:", arr)

    
    
    
    
    
    
    
    
    
arr = [2,6,5,1,7,4,3]

mergesort(arr)