import sys

input = sys.stdin.readline
N = int(input().rstrip())

nums = []
for mask in range(1, 1 << 10):          # 1 ~ 1023
    digits = [d for d in range(10) if mask & (1 << d)]
    num = 0
    for d in sorted(digits, reverse=True):
        num = num * 10 + d
    nums.append(num)

nums.sort()                              # 0, 1, 2, …, 9876543210

print(nums[N-1] if N <= len(nums) else -1)
