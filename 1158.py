from collections import deque

N, K = map(int, input().split())

class CircularQue:
    def __init__(self, N):
        self.N = N
        self.que = deque()
        for i in range(1, N + 1):
            self.que.append(i)
            
    def __len__(self):
        return len(self.que)
            
    def move(self, n):
        self.que.rotate(-n) # rotate() in deque.
    
    def eliminate(self, index):
        target_index = index % len(self.que)
        self.move(target_index)
        return self.que.popleft()
    
people = CircularQue(N)
eliminated = []

while people.que:
    eliminated.append(people.eliminate(K - 1))
    
print('<' + ', '.join(map(str, eliminated)) + '>')