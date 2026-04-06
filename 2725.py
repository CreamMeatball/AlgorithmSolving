import sys

input = sys.stdin.readline

C = int(input())
q = [int(input()) for _ in range(C)]
m = max(q)

phi = list(range(m + 1))

for i in range(2, m + 1):
	if phi[i] == i:
		for j in range(i, m + 1, i):
			phi[j] -= phi[j] // i
   
answer = [0] * (m + 1)

if m >= 1:
	answer[1] = 3
for i in range(2, m + 1):
	answer[i] = answer[i - 1] + (phi[i] << 1)
 
print('\n'.join(str(answer[n]) for n in q))