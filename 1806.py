N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
min_length = N + 1
sum_value = sum(numbers[start:end + 1])

while start <= end:
    # print(f"sum_value: {sum_value}. start: {numbers[start]}. end: {numbers[end]}")
    if sum_value >= S:
        length = end - start + 1
        # print(f"length: {length}")
        min_length = min(min_length, length)
        sum_value -= numbers[start]
        start += 1
    elif sum_value < S:
        if end == N - 1:
            break
        end += 1
        sum_value += numbers[end]
        
if min_length == N + 1:
    print(0)
else:
    print(min_length)