inputlist = [[] for _ in range(5)]

for i in range(5):
    temp = str(input())
    for j in range(len(temp)):
        inputlist[i].append(temp[j])
    
# print(inputlist)

for i in range(15):
    for j in range(5):
        try:
            print(inputlist[j][i], end="")
        except:
            continue