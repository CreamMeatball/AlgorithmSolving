import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    numbers = list(map(int, input().rstrip().split()))
    max_ = -float('inf')
    for i in range(N):
        temp_sum_ = sum(numbers[:i + 1])
        temp_max_ = temp_sum_
        for j in range(i):
            temp_sum_ -= numbers[j]
            temp_max_ = max(temp_max_, temp_sum_)
        max_ = max(max_, temp_max_)
    print(max_)