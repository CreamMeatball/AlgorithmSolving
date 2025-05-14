from collections import deque

target = list(map(int, input().split()))

# 딕셔너리의 key값은 immutable, hashable 해야하므로 list 불가
# 그렇기에 tuple()로 변환하여 key 값으로 사용해야함을 꼭 유의!!!
# 그렇게 변환된 tuple 값을 꺼내서 list() 로 변환하여 사용한 뒤, 다시 tuple()로 변환하여 넣어주는 식.

def A(cube):
    cube = list(cube)
    for i in range(4):
        cube[i], cube[7 - i] = cube[7 - i], cube[i]
    return tuple(cube)
        
def B(cube):
    cube = list(cube)
    temp3, temp4 = cube[3], cube[4]
    cube[3], cube[4] = cube[2], cube[5]
    cube[2], cube[5] = cube[1], cube[6]
    cube[1], cube[6] = cube[0], cube[7]
    cube[0], cube[7] = temp3, temp4
    return tuple(cube)
    
def C(cube):
    cube = list(cube)
    cube[1], cube[2], cube[5], cube[6] = cube[2], cube[5], cube[6], cube[1]
    return tuple(cube)
    
def D(cube):
    cube = list(cube)
    cube[0], cube[4] = cube[4], cube[0]
    return tuple(cube)

# visited에 단순히 “방문했음”만 표시하는 대신,
# “어떤 상태에서 어떤 연산을 통해 왔는지”를 같이 저장해 두면 역추적(back-tracking)이 가능함.
visited = {}
    
def bfs(target):
    start = (1,2,3,4,5,6,7,8)
    queue = deque([(start, 0)]) # deque(list()) 가 deque(1,2,3...) 같은 형태로 바꿔주는 것이기에, 값 두 개를 뭉쳐서 넣으려면 deque( list( tuple(a, b) ) )
    visited[tuple(start)] = (None, None)
    
    while queue:
        current, current_count = queue.popleft()
        
        if current == target:
            return current_count
        
        # next = A(current)
        # if next not in visited:
        #     visited[tuple(next)] = (current, 'A')
        #     queue.append((next, current_count + 1))
        # next = B(current)
        # if next not in visited:
        #     visited[tuple(next)] = (current, 'B')
        #     queue.append((next, current_count + 1))
        # next = C(current)
        # if next not in visited:
        #     visited[tuple(next)] = (current, 'C')
        #     queue.append((next, current_count + 1))
        # next = D(current)
        # if next not in visited:
        #     visited[tuple(next)] = (current, 'D')
        #     queue.append((next, current_count + 1))
        
        for op_name, op_func in [('A', A), ('B', B), ('C', C), ('D', D)]:
            next = op_func(current)
            if next not in visited:
                visited[tuple(next)] = (current, op_name)
                queue.append((next, current_count + 1))
            
count = bfs(tuple(target))
print(count)