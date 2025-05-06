import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())

words = []
for _ in range(N):
    words.append(str(input_data().rstrip()))
    
def isSimilar(A, B):
    A, B = list(A), list(B)
    pos_A, pos_B = {}, {}
    
    for i in range(len(A)):
        a, b = A[i], B[i]
        pos_A.setdefault(a, []).append(i)
        pos_B.setdefault(b, []).append(i)
            
    pos_A_set = set(tuple(v) for v in pos_A.values())
    pos_B_set = set(tuple(v) for v in pos_B.values())
    
    if pos_A_set == pos_B_set:
        return True
    return False
            
sets = set()            
            
for i in range(N - 1):
    for j in range(i + 1, N):
        if isSimilar(words[i], words[j]):
            sets.add((words[i], words[j]))
            
# print(sets)
print(len(sets))