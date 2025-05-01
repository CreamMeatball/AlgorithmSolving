import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())

files = []
for _ in range(N):
    files.append(str(input_data().rstrip()))

len_ = len(files[0])

result = list(files[0])

for i in range(N):
    for j in range(len_):
        if result[j] != '?' and files[i][j] != result[j]:
            result[j] = '?'
        
print(''.join(str(r) for r in result))