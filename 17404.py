import sys

input_ = sys.stdin.readline

N = int(input_().rstrip())
costs = []
for _ in range(N):
    costs.append(list(map(int, input_().rstrip().split())))
    
dp = [[0] * (N) for _ in range(3)]

for i in range()