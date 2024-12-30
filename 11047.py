import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().rstrip().split())
moneyList = [int(input_data().rstrip()) for _ in range(N)]

count = 0

while(K > 0):
    for i in range(N-1, -1, -1):
        if K >= moneyList[i]:
            count += K // moneyList[i]
            K %= moneyList[i] # 나머지 할당
            break
        
print(count)