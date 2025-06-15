import sys
from collections import Counter

input_ = sys.stdin.readline

n = int(input_().rstrip())

for _ in range(n):
    temp = list(map(int, input_().rstrip().split()))
    T = temp[0]
    soldiers = temp[1:]
    count = Counter(soldiers)
    for key, value in count.items():
        if value > (T // 2):
            print(key)
            break
    else:
        print("SYJKGW")