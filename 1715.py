from queue import PriorityQueue
Card = PriorityQueue()

N = int(input())

for i in range(N):
    Card.put(int(input()))
    
cost = 0
sum = 0

if N==0:
    cost = 0
else:
    for i in range(N-1):
        sum = Card.get() + Card.get()
        Card.put(sum)
        cost += sum
print(cost)