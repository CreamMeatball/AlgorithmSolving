import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

T = int(input_().rstrip())
for _ in range(T):
    N, K = map(int, input_().rstrip().split())
    Ds = [0] + list(map(int, input_().rstrip().split()))
    
    postorders = defaultdict(list)
    preorders = defaultdict(list)
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1) # "각 건물을 짓는데까지 걸리는 최소 시간"!! 풀면서 스스로 헷갈리지 말기.
    
    for _ in range(K):
        X, Y = map(int, input_().rstrip().split())
        postorders[X].append(Y)
        preorders[Y].append(X)
        indegree[Y] += 1
    
    W = int(input_().rstrip())
    
    dq = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            dq.append(i)
            dp[i] = Ds[i]
            
    while dq:
        current = dq.popleft()
        for next in postorders[current]:
            # dp[next] = max(dp[next], dp[current] + Ds[current]) # 오답 나오게 됨. += Ds[current] 를 아래에서 적용.
            # 틀리는 이유: 아래에서 틀리는 예시 설명.
            
            dp[next] = max(dp[next], dp[current]) # next의 preorder인 current가 먼저 건설이 필요한 시간과 비교
            indegree[next] -= 1
            if indegree[next] == 0:
                dq.append(next)
                dp[next] += Ds[next] # indegree가 모두 사라져 본인 건물이 건설 가능해졌으니 건설.
                # print(f"{next} is appended in dq")
        
    # print(f"final dp:")
    # print(dp)

    print(dp[W])
    

# [위 주석 코드가 틀리는 예시]
# 예를 들어 다음과 같은 건설 순서가 있다고 가정해봅시다:

# 건물 1: 건설 시간 10
# 건물 2: 건설 시간 20
# 건물 3: 건설 시간 30
# 오답 방식 (dp[next] = max(dp[next], dp[current] + Ds[current]))
# 건물 1 처리: dp[3] = max(0, 10 + 10) = 20
# 건물 1의 완성 시간(10) + **건물 1의 건설 시간(10)**을 더함
# 건물 2 처리: dp[3] = max(20, 20 + 20) = 40
# 건물 2의 완성 시간(20) + **건물 2의 건설 시간(20)**을 더함
# 결과: dp[3] = 40 (오답)
# 건물 3 자체의 건설 시간(30)이 누락됨
# 정답 방식
# 건물 1 처리: dp[3] = max(0, 10) = 10
# 건물 2 처리: dp[3] = max(10, 20) = 20
# 모든 선행 건물이 완료되면(indegree=0): dp[3] += 30
# 결과: dp[3] = 50 (정답)