import sys

def input_data():
    return sys.stdin.readline().rstrip()

S = str(input_data())
q = int(input_data())

for _ in range(q):
    alphabet, i, j = input_data().split()
    i, j = int(i), int(j)
    print(S[i:j + 1].count(alphabet))
