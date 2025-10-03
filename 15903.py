import heapq

n, m = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))
cards.sort()
# heapq.heapify(cards)
for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x + y)
    heapq.heappush(cards, x + y)
print(sum(cards))