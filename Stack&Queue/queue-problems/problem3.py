from collections import deque

def min_rounds_to_seat(heights):
    queue = deque(heights)
    rounds = 0
    while queue:
        rounds += 1
        new_queue = deque()
        prev = float('-inf')
        while queue:
            h = queue.popleft()
            if h > prev:
                prev = h
            else:
                new_queue.append(h)
        queue = new_queue
    return rounds

n = int(input())
heights = list(map(int, input().split()))
print(min_rounds_to_seat(heights))
