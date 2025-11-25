import math

def ln_fact(n):
    if n == 1:
        return 0
    return math.log(n) + ln_fact(n - 1)

n = 3
print(f"{ln_fact(n):.4f}")
