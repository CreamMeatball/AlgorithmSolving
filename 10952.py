import sys

sum = []

while(True):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0:
        break
    else:
        sum.append(a + b)
        
for result in sum:
    print(result)

