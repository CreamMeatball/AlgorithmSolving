import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

basket = [i for i in range(0, N+1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    for j in range(start, start+(end-start+1)//2):
        # 짝수일 때랑 홀수일 때랑 코드 같음
        temp = basket[j]
        basket[j] = basket[end-(j-start)]
        basket[end-(j-start)] = temp
        
for item in basket[1:]:
    print(item, end=' ')