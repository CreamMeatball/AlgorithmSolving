import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [0] * 1000002

for _ in range(N):
    S, E = map(int, input().split())
    arr[S] += 1
    arr[E + 1] -= 1

for i in range(1, 1000002):
    arr[i] += arr[i - 1]

Q = int(input().rstrip())
queries = map(int, input().split())

for q in queries:
    print(arr[q])