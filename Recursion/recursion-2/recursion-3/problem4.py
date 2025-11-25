def count_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways(n - 4) + count_ways(n - 8)

T = int(input())
for x in range(T):
    N = int(input())
    print(count_ways(N))
