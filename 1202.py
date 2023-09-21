import sys, heapq
input = sys.stdin.readline

NDia, NBag = map(int, input().split())

InfoDia = []
InfoBag = []

for _ in range(NDia):
    InfoDia.append(list(map(int, input().split())))

InfoBag = [int(input()) for _ in range(NBag)]

InfoDia.sort() # 보석 무게 오름차순 정렬. 무게 같은 경우엔 가치 오름차순으로 정렬.
InfoBag.sort() # 가방 크기 오름차순 정렬

maxDia = []
result = 0

for bag in InfoBag:
    while InfoDia and bag >= InfoDia[0][0]:
        heapq.heappush(maxDia, -InfoDia[0][1])
        heapq.heappop(InfoDia)
        
    if maxDia:
        result += heapq.heappop(maxDia)
    elif not InfoDia:
        break
    
print(-result)