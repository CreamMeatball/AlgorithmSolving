# 0, 1, 양수, 음수
# 를 나눠서 생각

# 1은 무조건 안 곱하고 더하는 게 크다
# 양수는 내림차순 정렬 뒤 큰 거부터 다 곱한다
# 음수는 오름차순 정렬 뒤 작은 거부터 다 곱한다
# 단 0은 음수 리스트에 포함시켜 처리한다

N = int(input())

positive = []
negative = []

total = 0


for _ in range(N):
    temp = int(input())
    if temp > 1: positive.append(temp)
    elif temp == 1: total += temp
    else: negative.append(temp)
    
positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        total += positive[i] * positive[i+1]
    else:
        total += positive[i]

        
for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        total += negative[i] * negative[i+1]
    else:
        total += negative[i]
        
print(total)
