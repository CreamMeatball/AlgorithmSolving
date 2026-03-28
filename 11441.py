import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

P = [0] * (N + 1)
for k in range(N):
    P[k+1] = P[k] + A[k]

for _ in range(M):
    i, j = map(int, input().split())
    print(P[j] - P[i-1])