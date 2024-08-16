import sys

T = int(sys.stdin.readline().rstrip())

case = [0 for _ in range(T)]

for i in range(T):
    case[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    
for i in range(T):
    # print("Case #", i+1, ": ", case[i][0] + case[i][1], sep='')
    print(f'Case #{i+1}: {case[i][0] + case[i][1]}')