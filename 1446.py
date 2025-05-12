import sys
import heapq

input_data = sys.stdin.readline

N, D = map(int, input_data().rstrip().split())
shortcut = {}
distance = [float('inf')] * (D + 1)

# 지름길 정보 입력
for _ in range(N):
    s, e, d = map(int, input_data().rstrip().split())
    if e <= D:  # 도착 위치가 고속도로 길이 D를 초과하지 않는 경우만 추가
        shortcut.setdefault(s, []).append((d, e))

def dijkstra(start):
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_dis, current_pos = heapq.heappop(queue)
        
        if current_dis > distance[current_pos]:
            continue
        
        # 일반 도로 이동 고려
        if current_pos + 1 <= D and current_dis + 1 < distance[current_pos + 1]:
            distance[current_pos + 1] = current_dis + 1
            heapq.heappush(queue, (current_dis + 1, current_pos + 1))
        
        if current_pos in shortcut:
            for next_dis, next_pos in shortcut[current_pos]:
                dist = current_dis + next_dis
                if dist < distance[next_pos]:
                    distance[next_pos] = dist
                    heapq.heappush(queue, (dist, next_pos))

dijkstra(0)
print(distance[D])