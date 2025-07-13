E, S, M = map(int, input().split())
year = 0
while True:
    year += 1
    if (year - 1) % 15 + 1 == E and (year - 1) % 28 + 1 == S and (year - 1) % 19 + 1 == M:
        print(year)
        break