N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

A.sort()

def binary_search(array, target, start, end):
    # print(f"start: {start}, end: {end}")
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search(array, target, mid + 1, end)
        else:
            return binary_search(array, target, start, mid - 1)
    return None

for x in X:
    result = binary_search(A, x, 0, N-1)
    if result != None:
        print(1)
    else:
        print(0)