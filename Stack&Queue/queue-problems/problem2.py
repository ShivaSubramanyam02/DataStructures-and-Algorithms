from collections import deque, Counter

def first_non_repeating(s):
    q = deque()
    count = Counter()
    result = []
    for ch in s:
        count[ch] += 1
        q.append(ch)
        while q and count[q[0]] > 1:
            q.popleft()
        result.append(q[0] if q else '-1')
    return ''.join(result)

s = input()
print(first_non_repeating(s))
