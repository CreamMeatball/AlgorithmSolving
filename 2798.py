N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sumOfNumbers = []

for i in range(N):
    sum = 0
    sum += numbers[i]
    for j in range(i+1, N):
        sum += numbers[j]
        for k in range(j+1, N):
            sum += numbers[k]
            if(sum <= M):
                sumOfNumbers.append(sum)
            sum -= numbers[k]
        sum -= numbers[j]
        
print(max(sumOfNumbers))