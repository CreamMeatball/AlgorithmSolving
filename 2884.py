H, M = map(int, input().split())

time = H*60 + M
timeEdit = time - 45

# -1 % 24 는 23 이 나오게 됨
print(timeEdit//60%24, timeEdit%60)