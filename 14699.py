import sys

input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    if heights[u-1] < heights[v-1]:
        adj[u-1].append(v-1)
    elif heights[v-1] < heights[u-1]:
        adj[v-1].append(u-1)
        
# 높은 위치의 쉼터부터 dp 계산을 진행하는 게 핵심!!!
# 왜냐면 높은 위치부터 정리해놔야, 이후 낮은 쉼터에서 사전 정리된 높은 쉼터에 도달했을 때 다시 계산하지 않고 기존 값으로 사용하여 효율적으로 진행할 수 있기 때문.

# 이렇게 하면,
# 현재 위치보다 높은 위치의 쉼터들이 이미 다 최적값이 게산돼있으니까
# 아래 쉼터의 입장에선 greedy하게 더 좋은 것만 쫓아가도 최적임이 보장됨.

# Bottom to Top 등산의 최적을 구하기 위해선
# 어차피 Top 에서부터의 값을 계산하게 됨.
# 이를 통해 Top --> Bottom 으로 계산해야겠구나, 라는 아이디어를 발견 가능.

order = sorted(range(N), key=lambda x: heights[x], reverse=True)
dp = [1] * N

for i in order:
    for nxt in adj[i]:
        if dp[nxt] + 1 > dp[i]:
            dp[i] = dp[nxt] + 1
            
for d in dp:
    print(d)