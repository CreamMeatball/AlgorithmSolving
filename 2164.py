import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

deck = deque()

for i in range(1, N+1):
    deck.append(i)

while(len(deck) > 1):
    deck.popleft()
    deck.append(deck.popleft())
    
print(deck[0])