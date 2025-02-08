import sys
from itertools import combinations # permutations(순열)도 있음

input_data = sys.stdin.readline

N, S = map(int, input_data().split())
numbers = list(map(int, input_data().split()))

count = 0

for i in range(1, N + 1):
    combs = combinations(numbers, i)
    for c in combs:
        if sum(c) == S:
            count += 1

print(count)