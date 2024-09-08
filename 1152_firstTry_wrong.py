S = str(input())

print(len(S) - len((''.join(S.split()))) + 1)