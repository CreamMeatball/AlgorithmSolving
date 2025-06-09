from collections import deque

N = int(input())

dropped = []
cards = deque([i for i in range(1, N + 1)])

while len(cards) > 1:
    dropped.append(cards.popleft())
    cards.append(cards.popleft())
    
dropped.append(cards.popleft())
print(*dropped)