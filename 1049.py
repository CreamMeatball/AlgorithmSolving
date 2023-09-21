import sys

input = sys.stdin.readline

cutString, numberOfBrand = map(int, input().split())

brandPrice = []

for _ in range(numberOfBrand):
    brandPrice.append(list(map(int, input().split())))   

leastSix = 1001
leastSolo = 1001

brandPrice.sort(key=lambda x:x[0])
leastSix = brandPrice[0][0]

brandPrice.sort(key=lambda x:x[1])
leastSolo = brandPrice[0][1]

least = 0

if leastSix < leastSolo*6:
    if leastSix < leastSolo * (cutString%6):
        least = leastSix * int(cutString/6 + 1)
    else:
        least = leastSix * int(cutString/6) + leastSolo * (cutString%6)
else:
    least = leastSolo * cutString

print(least)