N, M = map(int, input().split())

basket = [0 for i in range(N)]

for i in range(M):
    start, end, number = list(map(int, input().split()))
    for j in range(start-1, end):
        basket[j] = number
    # print(basket)
        
for item in basket:
    print(item, end=' ')