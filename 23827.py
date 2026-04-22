import sys

input = sys.stdin.readline
MOD = 1000000007

N = int(input())
A = list(map(int, input().split()))

total = sum(A)
answer = 0

for i in range(N):
    total -= A[i]
    answer = (answer + A[i] * total) % MOD

print(answer)