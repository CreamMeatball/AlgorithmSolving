import sys

input_data = sys.stdin.readline
N, K = map(int, input_data().split())

# 동생 위치가 정해져있기 때문에
# bfs로 풀어서 제일 먼저 도착하는 경우가 최단시간임이 보장될 거라고 예상됨
# 문제만 봤을 때는 dp 혹은 이진탐색 아닌가 싶지만 bfs로 될 거 같음

# 순간이동, 왼쪽걷기, 오른쪽걷기 3가지 경우가 있으므로
# node당 3개의 자식 노드를 주는 방향으로 bfs로 풀 수 있을 듯

visited = [False] * 100001
spend_time = [0] * 100001

def bfs(current_node, destination):
    global visited, spend_time
    queue = [current_node]
    visited[current_node] = True
    spend_time[current_node] = 0
    while queue:
        current_node = queue.pop(0)
        if current_node == destination:
            return spend_time[current_node]
        # 3가지 경우 확인 후 가능한 경우 queue에 추가
        for next_node in [current_node * 2, current_node - 1, current_node + 1]:
            if 0 <= next_node < 100001 and not visited[next_node]:
                visited[next_node] = True
                spend_time[next_node] = spend_time[current_node] + 1
                queue.append(next_node)
                
print(bfs(N, K))