from collections import deque

N, K = map(int, input().split())

max_len = 100000

# 처음부터 탐색을 해야되는 게 아니라 특정 위치부터 탐색을 해야돼서
# dp로는 못 풀 듯
# bfs로 풀어야 할 듯
# 그리고 선택지도 여러개라 dp보다는 더욱 bfs 쪽이 나은 듯

route = [-1] * (max_len + 1)
# 선택지가 3개가 있고, 후의 결정에 의해 전의 어떤 선택지가 최적인지가 달라짐 -> 방문한 곳을 또 방문할 수 있게 해놔야됨
# -> visited 사용 안 함

def bfs(n, k):
    queue = deque([n])
    route[n] = n # route[n] = x -> n 위치로 올 때 x 위치로부터 왔다는 뜻
    while queue:
        current = queue.popleft()
        
        if current == k: # 도착했으면, bfs니까 가장 먼저 도착한 애가 가장 빠른 경로
            # print(route[current])
            result = []
            while current != n: # route backtracking
                result.append(current)
                current = route[current]
            result.append(n)
            print(len(result) - 1)
            print(' '.join(map(str, result[::-1])))
            return
        
        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next <= max_len and route[next] == -1:
                route[next] = current
                queue.append(next)
                
bfs(N, K)