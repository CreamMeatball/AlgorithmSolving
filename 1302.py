import sys

N = int(sys.stdin.readline())

soldBooks = {}
bestCount = 0
bestSeller = []
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    if data not in soldBooks:
        soldBooks[data] = 1
        if bestCount < 1:
            bestCount = 1
    else:
        soldBooks[data] += 1
        if bestCount < soldBooks[data]:
            bestCount = soldBooks[data]
        
for key, value in soldBooks.items():
    if value == bestCount:
        bestSeller.append(key)
        
bestSeller.sort()
print(bestSeller[0])