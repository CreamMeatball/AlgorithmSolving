import sys
input_ = sys.stdin.readline
N = int(input_().rstrip())
numbers = []
for _ in range(N):
    numbers.append(str(input_().rstrip()))
len_ = len(numbers[0])

for k in range(1, len_ + 1):
    checklist = set()
    for n in numbers:
        cutn = n[len_ - k:]
        if cutn not in checklist:
            checklist.add(cutn)
        else:
            break
    else: # for문이 완전히 다 돌았을 경우
        print(k)
        break
