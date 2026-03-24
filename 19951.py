import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
diff = [0] * (N + 2)

for _ in range(M):
    a, b, k = map(int, input().split())
    diff[a] += k
    diff[b + 1] -= k

for i in range(1, N + 1):
    diff[i] += diff[i - 1]

for i in range(N):
    H[i] += diff[i + 1]

print(*H)
