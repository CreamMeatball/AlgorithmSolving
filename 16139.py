import sys

input = sys.stdin.readline
S = list(input().rstrip())
q = int(input().rstrip())

accum_count = [[0] * 26 for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    alphabet_index = ord(S[i - 1]) - ord('a')
    accum_count[i] = accum_count[i - 1][:]
    accum_count[i][alphabet_index] = accum_count[i - 1][alphabet_index] + 1
    
# for i, a in enumerate(accum_count):
#     if i != 0:
#         print(S[i-1], a)
#     else:
#         print(a)
    
for _ in range(q):
    alphabet, i, j = input().split()
    i, j = int(i), int(j)
    alphabet_index = ord(alphabet) - ord('a')
    print(accum_count[j + 1][alphabet_index] - accum_count[i][alphabet_index])