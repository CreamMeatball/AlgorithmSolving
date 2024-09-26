money = [25, 10, 5, 1]
number = int(input())

for _ in range(number) :
    totalmoney = int(input())
    rest = []

    for m in money :
        rest.append(totalmoney // m)
        totalmoney = totalmoney % m
        
    print(*rest)
