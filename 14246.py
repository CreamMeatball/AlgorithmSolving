n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

count = 0
current_sum = 0
start = 0

# 투포인터 + end 범위에 따른 start 범위 하나하나 다 brute-force.

for end in range(n):
    current_sum += numbers[end]

    while current_sum > k:
        count += (n - end)
        current_sum -= numbers[start]
        start += 1

print(count)