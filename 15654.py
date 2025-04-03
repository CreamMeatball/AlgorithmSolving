from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

permut = set()
for p in permutations(numbers, M):
    permut.add(p)
    
permut = sorted(permut)
# set()은 .sort()는 안되고 = sorted()만 되네
# set에 .sort() 메소드가 없음

for p in permut:
    print(*p)