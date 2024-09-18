def groupword(word):
    temp = "0"
    spell = []
    for w in word:
        if w != temp:
            if w in spell:
                return 0
            else:
                spell.append(temp)
                temp = w
        else:
            continue
    return 1

N = int(input())

count = 0

for i in range(N):
    word = input()
    count += groupword(word)
    
print(count)
        