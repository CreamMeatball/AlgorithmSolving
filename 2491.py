N = int(input())
numbers = list(map(int, input().split()))

dp_inc = [1] * N
dp_dec = [1] * N

for i in range(1, N):
    if numbers[i] >= numbers[i-1]:
        dp_inc[i] = dp_inc[i-1] + 1
        
    if numbers[i] <= numbers[i-1]:
        dp_dec[i] = dp_dec[i-1] + 1

print(max(max(dp_inc), max(dp_dec)))