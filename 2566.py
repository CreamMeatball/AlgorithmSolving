rows = 9
columns = 9
maxnumber = [0, [0, 0]]

item = []

for i in range(rows):
    item.append(list(map(int, input().split())))

for row in range(1, rows+1):
    for column in range(1, columns+1):
        if item[row-1][column-1] >= maxnumber[0]:
            maxnumber[0] = item[row-1][column-1]
            maxnumber[1] = [row, column]
            
print(int(maxnumber[0]))
print(int(maxnumber[1][0]), int(maxnumber[1][1]))