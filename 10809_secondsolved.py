S = str(input())

alphabet = map(chr, range(97, 123))
alphabet_list = [-1 for _ in range(26)]

alphabet_mapping = [(i,a) for i, a in enumerate(alphabet)]

for i, a in alphabet_mapping:
    if a in S:
        alphabet_list[i] = S.index(a)
        
for p in alphabet_list:
    print(p, end=' ')