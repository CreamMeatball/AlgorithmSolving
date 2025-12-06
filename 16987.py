import sys

input = sys.stdin.readline

N = int(input().rstrip())

eggs = []

for _ in range(N):
    d, w = map(int, input().rstrip().split())
    eggs.append([d, w])
    
# dfs + backtracking

# print(eggs)

result = 0

def dfs(index: int):
    # print(index)
    # print(eggs)
    if index == N:
        global result
        count = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                count += 1
        # print(f"count: {count}")
        result = max(result, count)
        return
    if eggs[index][0] <= 0:
        dfs(index + 1)
        return # 재귀 탈출해야됨
    
    check = False # 남은 계란들 중 안 깨진 계란이 있는지
    for i in range(N): # 잡은 계란으로부터 우측 계란만 칠 수 있는 게 아니라, 좌측 계란도 칠 수 있음. 유의.
        if i == index:
            continue
        if eggs[i][0] <= 0:
            continue
        check = True
        eggs[i][0] -= eggs[index][1]
        eggs[index][0] -= eggs[i][1]
        dfs(index + 1)
        # backtracking
        eggs[i][0] += eggs[index][1]
        eggs[index][0] += eggs[i][1]
    
    if not check:
        dfs(index + 1)
    # 이거 처리를 안 해주면,
    # 만약 손에 든 계랸이 안 깨진 상태에서, 다른 계란들이 모두 깨져있는 상태일 경우
    # for i in range(N) loop 를 돌면서 if eggs[i][0] <= 0: continue 에서 다 걸러지고 넘어가는 바람에
    # dfs(index + 1) 호출이 안됨.
    # 그래서 다음 계란으로 넘어가 계란을 드는 동작이 시동 되지 않음
    # 그러면 결국 이 route에서는 결론 도출 분기인 if index == N - 1: 을 못 타게 됨. 그래서 count가 안됨.
        
dfs(0)
print(result)