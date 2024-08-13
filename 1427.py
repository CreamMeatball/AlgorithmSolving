import sys

N = str(sys.stdin.readline().rstrip())

n = []

for i in range(len(N)):
    n.append(int(N[i]))
    
sorted_n = sorted(n, reverse=True)
print(''.join(str(sorted_n[i]) for i in range(len(sorted_n))))

