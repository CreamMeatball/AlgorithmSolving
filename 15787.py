import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# trains = [00000000000000000000] * (N + 1)
# 위처럼 0 여러개 그냥 쓰는 방식은 유효하지 않음. NameError 발생함.
trains = [0] * (N + 1)

for _ in range(M):
    data = list(map(int, input().rstrip().split()))
    if len(data) == 3:
        c, i, x = data
    elif len(data) == 2:
        c, i = data
    
    if c == 1:
        trains[i] |= (1 << (x - 1))
    elif c == 2:
        trains[i] &= ~(1 << (x - 1)) # 원하는 위치의 1만을 0으로 만들기 위한 트릭
    elif c == 3:
        # trains[i] = (trains[i] << 1) & ((1 << 20) - 1)
        trains[i] = (trains[i] << 1)
        trains[i] = trains[i] & (~(1 << 20)) # 20번쨰 좌석(19번째 비트) 넘어가는 좌석 0으로 만들기 위한 트릭. 혹은 아래의 더 간결한 방식
        # trains[i] &= ((1 << 20) - 1)
        # '- 1' 빼는 방식 작동 원리
        # 가장 오른쪽 비트에서 0 - 1을 할 수 없으니 왼쪽에서 빌려와야 합니다.
        # 왼쪽으로 계속 이동하다가 가장 왼쪽에 있는 1을 만납니다.
        # 이 1이 0이 되면서 오른쪽 비트에 2를 빌려줍니다.
        # 오른쪽 비트는 2를 빌려와서 1을 자신이가 갖고, 나머지 1을 또 오른쪽으로 넘겨줍니다. 이 과정이 연쇄적으로 반복됩니다.
        # 마지막 비트가 2를 빌려와 2 - 1을 계산하여 1이 됩니다.
        
    elif c == 4:
        trains[i] = (trains[i] >> 1) # 0번 비트에서 밀린 애는 자연스럽게 없어짐
        
# filter = [trains[0]]
# count = 1

# for i in range(1, N + 1):
#     data = filter[i]
#     for f in filter:
#         if f ^ data == 00000000000000000000:
#             break
#     else:
#         count += 1
#         filter.append(data)
        
# print(count)

passed_trains = set(trains[1:])
print(len(passed_trains))