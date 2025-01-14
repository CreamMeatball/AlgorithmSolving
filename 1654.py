import sys

input_data = sys.stdin.readline

K, N = map(int, input_data().rstrip().split())
ownCables = []
for i in range(K):
    ownCables.append(int(input_data().rstrip()))
    
ownCables.sort()
minLength = 1
maxLength = ownCables[-1]

maxCableLength = 0

def splitCable(array, length):
    cableCount = 0
    for cable in array:
        cableCount += cable // length
    return cableCount
    

# binary search for search the maxCableLength for making N cables when split cable
def binary_search(array, target, start, end):
    cableCount = 0
    global maxCableLength
    
    while start <= end:
        mid = (start + end) // 2
        cableCount = splitCable(array, mid)
        # 잘랐을 때 케이블 개수가 목표 개수 이상이다
        if cableCount >= target:
            # 잘린 케이블 길이가 최대다
            if mid > maxCableLength:
                maxCableLength = mid
            # 잘린 케이블 길이가 최대였어도 더 큰 게 없나 탐색
            return binary_search(array, target, mid + 1, end)
        # 잘랐을 때 케이블 개수가 목표 개수보다 적다
        elif cableCount < target:
            # 더 짧게 자르는 경우로 다시 탐색
            return binary_search(array, target, start, mid - 1)
    return None

binary_search(ownCables, N, minLength, maxLength)
print(maxCableLength)
        