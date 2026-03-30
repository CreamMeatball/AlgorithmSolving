import sys
input = sys.stdin.readline

# ab + ac + ad + bc + bd + cd
# = a(b + c + d) + b(c + d) + c(d)
# 로 정리하여, 누적합으로 효율적 계산.

N = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
answer = 0

for x in arr:
    total_sum -= x
    answer += x * total_sum

print(answer)