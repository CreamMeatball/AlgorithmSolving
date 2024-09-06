S = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(map(str, alphabet))

sequence = [-1 for _ in range(26)]

for i in range(len(S)):
    for s in S:
        sequence[alphabet_list.index(s)] = S.index(s)
        
for p in sequence:
    print(p, end=' ')