def recursive_sum(arr, n):
    
    if n == 0:
        return 0

    return arr[n-1] + recursive_sum(arr, n-1)



t = int(input())

for x in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))
    print(recursive_sum(arr, n)) 




