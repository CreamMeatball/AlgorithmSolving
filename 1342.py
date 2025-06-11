# from itertools import permutations
from collections import Counter

S = list(str(input()))

N = len(S)

# def islucky(word: list, N):
#     for i in range(N):
#         if i == 0:
#             if word[i] == word[i + 1]:
#                 return False
#         elif i == N - 1:
#             if word[i - 1] == word[i]:
#                 return False
#         else:
#             if word[i - 1] == word[i] or word[i] == word[i + 1]:
#                 return False
#     return True

count = 0

# for s in set(permutations(S, N)):
#     # print(s)
#     if islucky(s, N):
#         count += 1

counter_s = Counter(S)
def dfs(prev: str, depth: int):
    global count
    if depth == N:
        count += 1
        return
    
    for key, value in counter_s.items():
        if value > 0 and key != prev:
            counter_s[key] -= 1
            dfs(key, depth + 1)
            counter_s[key] += 1
    
dfs('', 0)

print(count)