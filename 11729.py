# 가장 큰 원판이 최종적으로 도착해야 할 위치로 이동해야함
# 이 때, 이를 위해 가장 큰 원판의 바로 위에 있던 원판이 도착해야 할 위치는,
# 가장 큰 원판이 있었던 시작 위치 기둥과 도착해야할 도착 위치 기둥을 제외한 나머지 한 기둥의 위치임.

# 궁극적인 시작 위치의 기둥을 시작 기둥, 도착 위치의 기둥을 도착 기둥, 나머지 기둥을 보완 기둥이라고 할 때,
# 결국 각 단계에서 가장 큰 원판이 도착 위치로 이동하기 위해서
# 바로 전 단계의 가장 큰 원판의 도착 위치는 보완 기둥이 되어야 함.
# 이와 같은 내용을 기반으로 재귀를 작성함.

def hanoi(n, start, end, supplement, moves):
    global count
    if n == 1:
        moves.append([start, end])
        return
    
    # n개의 하노이 원판을 올길 때는 다음과 같은 과정을 거침
    # 1. n-1 개의 원판을 보완 기둥으로 옮김
    # 2. 가장 큰 원판을 도착 기둥으로 옮김
    # 3. 옮겼던 n-1 개의 원판을 도착 기둥으로 옮김(가장 큰 원판 위)
    # 해당 과정을 아래 코드로 구현
    
    # 1.
    hanoi(n - 1, start, supplement, end, moves)
    # 2.
    moves.append([start, end])
    # 3.
    hanoi(n - 1, supplement, end, start, moves)

N = int(input())

moves = []

hanoi(N, 1, 3, 2, moves)

print(len(moves))
for move in moves:
    print(move[0], move[1])