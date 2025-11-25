def count_ones_in_binary(n):
    result = []
    for i in range(n + 1):
        count = bin(i).count('1')  # convert to binary and count 1s
        result.append(count)
    return result

T = int(input())
for binary in range(T):
    n = int(input())
    ans = count_ones_in_binary(n)
    print(*ans)
