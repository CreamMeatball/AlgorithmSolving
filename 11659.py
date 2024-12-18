import sys

def sys_input():
    return sys.stdin.readline().rstrip()

N, M = map(int, sys_input().split())

# print(N, M)

numbers = list(map(int, sys_input().split()))

accum_sum = [numbers[0]]
for i in range(1, N):
    accum_sum.append(accum_sum[-1] + numbers[i])
    
# print(accum_sum)

for _ in range(M):
    a, b = map(int, sys_input().split())
    if a >= 2:
        print(accum_sum[b-1] - accum_sum[a-2])
    else:
        print(accum_sum[b-1])
