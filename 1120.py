A, B = map(str, input().split())

lendiff  = len(B) - len(A)

def countdiff(A, B):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff += 1
    return diff

if lendiff == 0:
    print(countdiff(A, B))
elif lendiff > 0:
    mindiff = 50
    for startindex in range(lendiff + 1):
        Btemp = B[startindex:startindex + len(A)]
        diff = countdiff(A, Btemp)
        if diff < mindiff:
            mindiff = diff
    print(mindiff)