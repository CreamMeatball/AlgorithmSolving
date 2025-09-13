N = int(input())
numbers = list(map(int, input().split()))

sums = [0] * N

for i in range(N):
    sums[i] = numbers[i]
    for j in range(i):
        if numbers[j] < numbers[i]:
            sums[i] = max(sums[i], sums[j] + numbers[i])
    # print(f"i: {i}")
    # print(sums)
                
print(max(sums))