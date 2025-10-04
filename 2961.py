N = int(input())
ingreds = []
for _ in range(N):
    ingreds.append(tuple(map(int, input().split())))
    
min_diff = float('inf')

# 비트마스킹.
# 각 자리를 각 재료라고 치환.
# 0101 이면 0번째 재료와 2번째 재료를 사용한다는 뜻.

for i in range(1, 1 << N):
    total_sour = 1 # 신맛은 곱셈이므로 1로 초기화
    total_bitter = 0 # 쓴맛은 덧셈이므로 0으로 초기화

    for j in range(N):
        if (i >> j) & 1:
            sour, bitter = ingreds[j]
            total_sour *= sour
            total_bitter += bitter

    current_diff = abs(total_sour - total_bitter)

    min_diff = min(min_diff, current_diff)

print(min_diff)