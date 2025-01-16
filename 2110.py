import sys

input_data = sys.stdin.readline

N, C = map(int, input_data().rstrip().split())
houseCoord = []
for _ in range(N):
    houseCoord.append(int(input_data().rstrip()))
houseCoord.sort()
# print(houseCoord)

minDist = 1
maxDist = houseCoord[-1] - houseCoord[0]

answer = 1

def binary_search(array, target, start, end):
    global answer
    if start > end:
        return None
    
    mid = (start + end) // 2
    count = 1
    # print(f"[bs] start: {start}, target: {target}, end: {end}, mid: {mid}")
    
    coordFlag = array[0]
    
    for i in range(1, len(array)):
        if array[i] - coordFlag >= mid:
            count += 1
            coordFlag = array[i]
    
    # == 가 아닌 >= 가 맞음. 왜냐면 간격을 덜 벌려서 count가 높아진다고 해도,
    # 그건 곧 공유기를 count만큼 설치한다는 게 아니라 최대 count까지 설치할 수 있다는 의미이기 때문에
    # count > target 이더라도 정답이 될 수 있음(공유기를 C개만큼만 설치하면 되는 거기 때문에)
    # 또한 특정 케이스에 따라 count == target이 되지 않는 경우가 있을 수 있고, 이 경우엔 count > target인 경우가 가능한 최대 거리, 즉 정답이기 때문에
    # 꼭 >= 여야 함
    if count >= target:
        answer = mid
        # print(f"updated. answer: {answer}")
        return binary_search(array, target, mid + 1, end)
    elif count < target:
        # print(f"count < target. count: {count}, mid : {mid}")
        return binary_search(array, target, start, mid - 1)
    
binary_search(houseCoord, C, minDist, maxDist)
print(answer)