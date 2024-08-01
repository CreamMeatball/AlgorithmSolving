N, M = map(int, input().split())

numbers = list(map(int, input().split()))
    
sortedNumbers = sorted(numbers, reverse=True)

forMaximum = []

for i in range(N-2):
    temp = 0
    count = 3
    for j in range(i, N):
        if(count == 0):
            break
        if((temp+sortedNumbers[j] <= M)):
            temp += sortedNumbers[j]
            count -= 1
        else:
            continue
    forMaximum.insert(i, temp) if count == 0 else forMaximum.insert(i, 0)

# print(sortedNumbers)
print(max(forMaximum))
                
# 0번째 탐색 -> 0번째+temp(지금까지 합)<=M일 경우
# 0번째 더함
# 1번째 탐색 -> 1번째+temp(지금까지 합)<=M일 
# 1번째 더함
# 2번째 탐색 -> 2번째+temp(지금까지 합)<=M일 경우
# 2번째 더함
# 아닐 경우
# 3번째 탐색
# 총 더한 횟수가 3번이면 종료