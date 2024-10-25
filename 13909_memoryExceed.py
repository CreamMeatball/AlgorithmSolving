import sys

N = int(sys.stdin.readline().rstrip())

# window = [-1 for _ in range(N+1)]
window = {}

for i in range(2, N+1):
    for j in range(i, N+1, i):
        try:
            window[j] *= -1
        except:
            window[j] = -1
            
# print(window)
        
print(N - sum(-value for value in window.values() if value == -1))