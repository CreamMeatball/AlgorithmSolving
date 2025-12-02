N = int(input())
A = list(map(int, input().split()))

possible_remainders = {0}

for duration in A:
    new_remainders = set()
    for r in possible_remainders:
        # 기존 나머지에 현재 일의 기간을 더하고 7로 나눔
        next_r = (r + duration) % 7
        new_remainders.add(next_r)
    
    # 기존 집합에 새로운 나머지들을 추가
    possible_remainders.update(new_remainders)
    
    if len(possible_remainders) == 7: # 모든 날 다 가능해지면 그냥 중단
        break
        
# 모든 가능한 나머지들을 저장해놓고, 현재까지의 모든 나머지들에 각각 다 연산해주는 방식이기에
# 일의 시간 순서가 고려됨.

# 추가적으로, 일의 순서를 변경 = 특정 일들만 선택적으로 선별. 동치임.
        
if 4 in possible_remainders:
    print("YES")
else:
    print("NO")