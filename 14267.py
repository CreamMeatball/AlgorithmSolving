import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
bosses = [0] + list(map(int, input().split()))

compliment = [0] * (n + 1)
for _ in range(m):
    junior, w = map(int, input().split())
    compliment[junior] += w

# print(bosses)
# print(compliment)

tree = defaultdict(list) # boss: juniors
for i in range(2, n + 1):
    boss = bosses[i]
    tree[boss].append(i)
    
# print(tree)

dp = [0] * (n + 1)
dp[1] = compliment[1]

for key, values in tree.items():
    for value in values:
        dp[value] = dp[key] + compliment[value]
        
print(*dp[1:])


# 테스트 케이스
# 입력
# 6 3
# -1 1 1 2 2 3
# 2 2
# 2 3
# 6 5

# 0 5 0 5 5 5