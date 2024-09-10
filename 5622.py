Word = str(input())

dic = dic = {('A', 'B', 'C'): 3, ('D', 'E', 'F'): 4, ('G', 'H', 'I'): 5, ('J', 'K', 'L'): 6, ('M', 'N', 'O'): 7, ('P', 'Q', 'R', 'S'): 8, ('T', 'U', 'V'): 9, ('W', 'X', 'Y', 'Z'): 10}

cost = 0

for index, (key, value) in enumerate(dic.items(), start=0):
    for w in Word:
        if w in key:
            cost += value
            
print(cost)