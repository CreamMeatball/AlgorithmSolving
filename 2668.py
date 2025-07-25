import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

numbers = [0] + list(int(input().rstrip()) for _ in range(N))

sameSet = set([])
for i, n in enumerate(numbers):
    if i == n:
        sameSet.add(n)
sameSet.remove(0)

for start in range(1, N + 1):
    # print(f"start: {start}")
    visited = [False] * (N + 1)
    stack = deque([start])
    parentSet = set([start])
    childSet = set([])
    while stack:
        parent = stack.pop()
        parentSet.add(parent)
        child = numbers[parent]
        childSet.add(child)
        # print(f"{parent} -> {child}")
        if not visited[child]:
            stack.append(child)
            visited[child] = True
            
    # print(f"is it same? parentSet: {parentSet} ?= childSet: {childSet}")
    if parentSet == childSet:
        # print(f"Yes")
        # 가능한 경우들(사이클)을 모두 합쳐야 됨.
        sameSet = sameSet.union(parentSet)
        
sameSet = sorted(list(sameSet))
print(len(sameSet))
for n in sameSet:
    print(n)
    