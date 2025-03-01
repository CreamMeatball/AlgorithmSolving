N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

start, end = 0, N - 1
min_sum = float('inf')
min_pair = (0, 0)

while start < end:
    temp_sum = liquids[start] + liquids[end]
    if abs(temp_sum) < min_sum:
        min_sum = abs(temp_sum)
        min_pair = (liquids[start], liquids[end])
    if temp_sum < 0:
        start += 1
    else:
        end -= 1
        
print(min_pair[0], min_pair[1])