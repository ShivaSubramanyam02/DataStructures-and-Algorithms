def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

T = int(input())
for x in range(T):
    N = int(input())
    binary = to_binary(N)
    if binary == "":
        print("0")
    else:
        print(binary)

