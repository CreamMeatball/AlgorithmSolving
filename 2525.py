H, M = map(int, input().split())
require = int(input())

time = H*60 + M
timeEdit = time + require
print(timeEdit//60%24, timeEdit%60)