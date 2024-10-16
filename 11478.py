inputstr = str(input())

partialset = set()

for i in range(1, len(inputstr)+1):
    for j in range(len(inputstr)-i+1):
        partialset.add(inputstr[j:j+i])

print(len(partialset))
