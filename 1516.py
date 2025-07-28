import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())

postfix_detail = defaultdict(list)
timecost = [0] * (N + 1)
for i in range(1, N + 1):
    data = list(map(int, input().rstrip().split()))
    timecost[i] = data[0]
    postfix_detail[i].extend(data[1:])
    
print(postfix_detail)