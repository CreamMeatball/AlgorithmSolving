# PyPy3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

R, C = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = (0, 0)
start_bit = 1 << (ord(board[0][0]) - ord('A'))
max_count = 0

def dfs(mask: int, pos, count): # set() 으로 탐색한 알파벳 저장 및 확인하는 방식에서 bitmask 방식으로 변경
    # PyPy3에서, 경로 저장-탐색 방식에 따른 시간 소요 -> set() 방식: 7064ms / bitmask 방식: 4564ms
    global max_count
    max_count = max(max_count, count)
    
    r, c = pos
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (0 <= nr < R) and (0 <= nc < C):
            na = board[nr][nc]
            bit = 1 << (ord(na) - ord('A'))
            # print(f"na: {na}. As: {As}")
            # if na not in As: # 매번 'in' 탐색을 해야하는데, list면 O(n)이고 set이면 평균 O(1). 시간 면에서 훨씬 효율적임.
            #     dfs(As, (nr, nc), count + 1)
            if not (mask & bit):
                dfs(mask | bit, (nr, nc), count + 1)
    # As.remove(a) # mutable 인자는 파라미터 내에 저장하는 방식이어도, 부모/형제 호출 모두에 대해서 변경됨. 그래서 remove / pop(list의 경우) 해줘야됨
                
dfs(start_bit, start, 1)
                
print(max_count)

# [bitmask 방식 원리]
# 알파벳 26개가 있고, 각 알파벳이 경로에 포함됐는지 아닌지를 26칸짜리 스위치로 생각.
# 1        # 2진수: 0001
# 1 << 0   # 0001 (1)
# 1 << 1   # 0010 (2)
# 1 << 2   # 0100 (4)
# 1 << 3   # 1000 (8)
# 1 << 4   # 10000 (16)
# 1 << 5   # 100000 (32)
# ...

# 그래서 현재의 탐색 알파벳이 C면
# bit = 1 << (ord(na) - ord('A')) 를 통해 bit = 1 << 2 라서 bit = 4 (0100) 이 되고
# 이걸 누적 알파벳 탐색 정보인 mask과 bitwise 연산(&, |)을 했을 때,
# 안 겹치면 기존 탐색했던 경로에 없었다는 걸로 판단하는 방식.

# 기존 set()을 사용했던 방식보다 훨씬 시간 효율적임.
# backtracking을 위해 굳이 pop / remove 처리해주지 않아도 됨.

# [bitmask 방식 제한]
# 사용 가능한 때:
# 1) 상태의 종류가 작고 고정적일 때
# 2) 방문 여부만 체크하면 되는 경우

# 1) -> 상태 개수가 너무 많으면 메모리 초과됨. 알파벳은 26개라서 괜찮은데 만약 100개면 2^100 이라서 10**30 을 초과하는 값이기에 압도적으로 커짐.
# 2) -> 알파벳처럼 각각 개별적인 종류의 탐색 유무를 판단하는 경우에 적합함.