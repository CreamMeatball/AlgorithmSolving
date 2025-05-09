import sys

input_data = sys.stdin.readline

N, C, W = map(int, input_data().rstrip().split())

logs = []
for _ in range(N):
    logs.append(int(input_data().rstrip()))
    
def cut(logs, C, W):
    max_earn = 0
    for length in range(1, max(logs) + 1):
        total_profit = 0
        for log in logs:
            cutnumber, cutlogs = calculate(log, length)
            revenue = cutlogs * length * W
            cost    = cutnumber * C
            profit  = revenue - cost
            # 이 통나무가 양수 이익일 때만 합산
            # 이 조건분기를 무조건 해줘야 됨.
            # 안 그러면 cut 비용이 너무 커서 
            # 어떠한 통나무를 자르면 오히려 손해가 발생하는 경우에도
            # 손해를 감수하고 자르게 됨.
            # 예를 들어 cut비용 100, 자르려는 목표길이 16, 통나무 길이 30, 나무 한 단위 가격 6이면
            # 자르면 통나무가 16 / 14로 나뉘어서 14는 버려지고 16만 쓰는데
            # 16 * 6 - 100 하면 -4원임.
            if profit > 0:
                total_profit += profit
        
        if total_profit > max_earn:
            max_earn = total_profit
                
    return max_earn

def calculate(log, length):
    cutlogs = log // length
    if cutlogs == 0: # 자르려는 목표 길이보다 애초에 통나무 길이가 작을 경우를 고려해줘야 함.
        return 0, 0
    cutnumber = cutlogs - 1 if log % length == 0 else cutlogs
    return cutnumber, cutlogs

result = cut(logs, C, W)
print(result)