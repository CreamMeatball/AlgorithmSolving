def cantor(line):
    s = 0
    e = len(line)
    return cantor(line[s:e//3]) + " " * (e//3) + cantor(line[s + 2 * e//3:e]) if e > 1 else "-"

while(True):
    try:
        N = int(input())
        print(cantor('-' * (3 ** N)))
    except:
        break