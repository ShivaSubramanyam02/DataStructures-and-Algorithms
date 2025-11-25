def count_common_elements(A: list, B: list, n: int) -> None:
    B.reverse()  
    
    i = 0 
    j = 0
    count = 0
    
    while i < n and j < n:
        if A[i] == B[j]:
            count+=1
            i+=1
            j+=1
            
        elif A[i] < B[j]:
            i+=1
            
        else:
            j+=1
            
    print(count)

count_common_elements([1, 2, 4, 5, 6],[6, 5, 3, 2, 1],n = 5)            