import sys
input_ = sys.stdin.readline

N = int(input_())
cranes = sorted(map(int, input_().split()), reverse=True)
M = int(input_())
boxes = sorted(map(int, input_().split()), reverse=True)

visited = [False]*M
pos = [0]*N # 각 크레인이 다음에 확인할 박스 인덱스
moved = 0
time = 0

if boxes[0] > cranes[0]:
    print(-1)
else:
    while moved < M:
        time += 1
        for i in range(N): # 크레인 선택
            # 이전에 마지막으로 옮겼던 박스 위치 이후부터, 이 크레인이 옮길 수 있는 박스 위치까지 pos[i]를 옮긴다
            while pos[i] < M:
                if not visited[pos[i]] and cranes[i] >= boxes[pos[i]]: # 이동시킬 수 있을 때
                    visited[pos[i]] = True
                    moved += 1
                    pos[i] += 1
                    break
                pos[i] += 1 # 이동시킬 수 없을 때

    print(time)