N, M = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()

def cuttedTreeSum(treeList, length):
    sumOfCuttedTree = 0
    for tree in treeList:
        if tree > length:
            sumOfCuttedTree += tree - length
            # print(f"sumOfCuttedTree: {sumOfCuttedTree}")
    return sumOfCuttedTree

maxTreeHeight = tree[-1]
minTreeHeight = 0
maxCutLength = 0

def binary_search(array, target, start, end):
    global maxCutLength
    if start > end:
        return None
    mid = (start + end) // 2
    # print(f"mid: {mid}")
    cuttedTree = cuttedTreeSum(array, mid)
    if cuttedTree >= target:
        if mid > maxCutLength:
            maxCutLength = mid
            # print(f"maxCutLength updated: {maxCutLength}")
        return binary_search(array, target, mid + 1, end)
    elif cuttedTree < target:
        return binary_search(array, target, start, mid - 1)
    
binary_search(tree, M, minTreeHeight, maxTreeHeight)
print(maxCutLength)