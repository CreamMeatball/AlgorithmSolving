from collections import deque

def dfs(depth, numbers, prev, result):
    if depth == M:
        print(" ".join(map(str, result)))
        return
    for number in numbers:
        if number < prev:
            continue
        result.append(number)
        dfs(depth + 1, numbers, number, result)
        result.pop()
        

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = deque()

dfs(0, numbers, 0, result)