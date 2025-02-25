X = int(input())

sticks = [64]

while sum(sticks) != X:
    target = int(sticks.pop(0))
    half = target // 2
    if sum(sticks) + half >= X:
        sticks.insert(0, half)
    else:
        sticks.insert(0, half)
        sticks.insert(0, half)
print(len(sticks))
