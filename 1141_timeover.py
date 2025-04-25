import sys
from itertools import combinations

input_data = sys.stdin.readline

def is_notprefix_subset(subset):
    for i, s1 in enumerate(subset):
        for j, s2 in enumerate(subset):
            if i == j:
                continue
            if s1 == s2[:len(s1)]:
                return 0
    # print(f"notprefix subset: {subset}")
    return len(subset)

N = int(input_data().rstrip())

words = []

for _ in range(N):
    words.append(input_data().rstrip())

maxlen = 0

for i in range(1, N + 1):
    combs = combinations(words, i)
    for comb in combs:
        len_ = is_notprefix_subset(comb)
        if len_ > maxlen:
            maxlen = len_
            
print(maxlen)