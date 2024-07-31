testCaseNum = int(input())

N = []
M = []

for i in range(testCaseNum):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)
    
for i in range(testCaseNum):
    print(N[i], M[i])