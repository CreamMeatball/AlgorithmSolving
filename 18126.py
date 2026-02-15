import sys
input = sys.stdin.readline
N = int(input().rstrip())
if N == 1: print(0); exit()
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w)); adj[v].append((u, w))

dist = [-1] * (N + 1); dist[1] = 0
q = [1]; ans = 0
for u in q:
    ans = max(ans, dist[u])
    for v, w in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + w
            q.append(v)

print(ans)
