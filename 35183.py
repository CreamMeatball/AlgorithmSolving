import sys

input = sys.stdin.readline

N = int(input())
can0 = [False] * 1002 # 광역기 한 번도 안 맞고 i까지 도달할 수 있는가?
can1 = [False] * 1002 # 광역기 한 번 맞고 i까지 도달할 수 있는가?

for i in range(N):
    l, r = map(int, input().split())
    nxt0 = [False] * 1002
    nxt1 = [False] * 1002
    
    if i == 0:
        for p in range(1, 1001):
            if l <= p <= r:
                nxt0[p] = True
            nxt1[p] = True
    else:
        for p in range(1, 1001):
            near0 = can0[p-1] or can0[p] or can0[p+1] # 현재 탐색 위치 p에 도달할 수 있는 위치 중에서 하나라도 안 맞고 도달한 경우가 있냐 --> 있어야 다음의 nxt0 이 True 가 될 수 있는 가능성이 있음.
            near1 = can1[p-1] or can1[p] or can1[p+1]
            
            if near0 and l <= p <= r:
                nxt0[p] = True
            if (near1 and l <= p <= r) or near0:
                nxt1[p] = True
                
    can0, can1 = nxt0, nxt1 # 이중 루프 구조로써, 하나의 i 탐색에서 p 루프 탐색이 독립적으로 이뤄져야 하기 때문에, p 탐색 시 이전 p 값으로 인한 값 변동을 받지 않기 위해 can과 nxt 변수 2개로 분리하여 사용.
    if not any(can1):
        break

print("World Champion" if any(can1) else "Surrender")