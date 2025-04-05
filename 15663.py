from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

permt = set()

for p in permutations(numbers, M):
    permt.add(p)
    
permt = sorted(permt)

for p in permt:
    print(*p)