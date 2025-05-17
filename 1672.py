N = int(input())
dna = list(str(input()))

table = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T']
]

table_index = {
    'A': 0,
    'G': 1,
    'C': 2,
    'T': 3
}

while (len(dna) > 1):
    a = dna.pop()
    b = dna.pop()
    if a == b:
        new = a
    else:
        i = table_index[a]
        j = table_index[b]
        new = table[j][i]
    dna.append(new)
    # if use str slicing, it spend too long. 
    # so, do str to list parsing and use pop()
    
print(''.join(dna))
