import sys
input = sys.stdin.readline

N = int(input().rstrip())
circles = []

# 원 두 개 골라서 내접 외접 판단하는 원론적 방식으로 그냥 푸니까 시간 초과 남

# stack의 관점으로 접근하여 풀이하기
# (참고: https://velog.io/@leetaekyu2077/Python-%EB%B0%B1%EC%A4%80-22942%EB%B2%88-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B2%B4%EC%BB%A4 )
# 원의 왼쪽 x절편: ( 또는 [
# 원의 오른쪽 x절편: ) 또는 ]
# 이라고 할 때

# 접하지 않는 경우
# ( [ ] )  # 원의 내부에서 접하지 않음
# ( ) [ ]  # 원의 외부에서 접하지 않음

# 접하는 경우
# ( [ ) ]

# stack 관점으로 보아서, 괄호가 순서에 맞게 열리고 닫히면 접하지 않음, 그렇지 않으면 접함(교점 생김)

for i in range(N):
    x, r = map(int, input().rstrip().split())
    circles.append((x-r, i)) # 원의 왼쪽 x절편
    circles.append((x+r, i)) # 원의 오른쪽 x절편
circles.sort()

stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop() # 열리고 닫힘
            continue
    stack.append(c) # 새로 열림
    
# 다 진행나고 나서, 스택 내부에 값이 존재하지 않으면
# 정상적으로 다 열리고 닫혔단 뜻이므로, 모든 원이 서로 접하지 않음

if not stack:
    print("YES")
else:
    print("NO")