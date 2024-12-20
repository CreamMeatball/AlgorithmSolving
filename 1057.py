N, jimin, hansu = map(int, input().split())
count = 0
while jimin != hansu:
    jimin -= jimin // 2
    hansu -= hansu // 2
    count += 1
print(count)