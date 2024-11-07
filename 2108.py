import sys

N = int(sys.stdin.readline().rstrip())

number = list(int(sys.stdin.readline().rstrip()) for _ in range(N))

number = sorted(number)

count = 0
current_number = 0
mode = 0
current_mode = [[0, 0]]
for n in number:
    if not (n == current_number):
        if count > current_mode[0][1]:
            current_mode = [[current_number, count]]
        elif count == current_mode[0][1]:
            current_mode.append([current_number, count])
        current_number = n
        count = 0
    count += 1
    if n == number[-1]:
        if count > current_mode[0][1]:
            current_mode = [[current_number, count]]
        elif count == current_mode[0][1]:
            current_mode.append([current_number, count])

# print(current_mode)

# print("산술평균")
print(int(round(sum(number) / N, 0)))
# print("중앙값")
print(number[N // 2])
# print("최빈값")
if len(current_mode) > 1:
    print(current_mode[1][0])
else:
    print(current_mode[0][0])
# print("범위")
print(number[N-1] - number[0])