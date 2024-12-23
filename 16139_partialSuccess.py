S = str(input())
q = int(input())

numberOfAlphabets = [[0] * 26 for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(26):
        numberOfAlphabets[i][j] = numberOfAlphabets[i - 1][j] + (1 if ord(S[i - 1]) - ord('a') == j else 0)
        
for _ in range(q):
    alphabet, i, j = input().split()
    i, j = int(i), int(j)
    print(numberOfAlphabets[j + 1][ord(alphabet) - ord('a')] - numberOfAlphabets[i][ord(alphabet) - ord('a')])
    
