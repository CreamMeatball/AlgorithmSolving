# 시간 초과 때문에 PyPy3로 제출

import sys
from collections import deque

input_data = sys.stdin.readline

class DSLR:
    def __init__(self):
        self.max_len = 10000
        self.command_list = ['D', 'S', 'L', 'R']
        
    def command(self, c, n):
        if c == 'D':
            return self.D(n)
        elif c == 'S':
            return self.S(n)
        elif c == 'L':
            return self.L(n)
        elif c == 'R':
            return self.R(n)
    
    def D(self, n):
        return (n * 2) % self.max_len
    
    def S(self, n):
        return n - 1 if n != 0 else 9999
    
    def L(self, n):
        # n_str = str(n)
        # n_str = n_str[1:] + n_str[0]
        # return int(n_str)
        return (n % 1000) * 10 + (n // 1000)
    
    def R(self, n):
        # n_str = str(n)
        # n_str = n_str[-1] + n_str[:-1]
        # return int(n_str)
        return (n % 10) * 1000 + (n // 10)

    def bfs(self, a, b): # save the route of commands
        route = [-1] * (self.max_len + 1)
        queue = deque([a])
        route[a] = a
        while queue:
            current = queue.popleft()
            
            if current == b:
                result = []
                while current != a:
                    result.append(route[current][1])
                    current = route[current][0]
                return ''.join(result[::-1])
            
            for c in self.command_list:
                next = self.command(c, current)
                if route[next] == -1:
                    route[next] = (current, c)
                    queue.append(next)
        

T = int(input_data())

for _ in range(T):
    A, B = map(int, input_data().rstrip().split())
    d = DSLR()
    d_bfs = d.bfs(A, B)
    print(d_bfs)