A, B = map(int, input().split())
if A > B:
    A, B = B, A
# result = (A + B) * (B - A + 1) / 2
result = B*(B+1)//2 - A*(A-1)//2
print(result)