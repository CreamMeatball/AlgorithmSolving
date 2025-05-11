input_ = str(input())
times = list(map(int, input_.split(':')))
num = 0
# 0: minutes or seconds
# 1-12: minutes or seconds or hours
# 13-59: minutes or seconds
# 60-99: None

# min_or_secs = 0
# all = 0
# for t in times:
#     if t > 59: # 59가 초과되는 숫자가 하나라도 있는 이상 정상적인 시간으로 읽을 수 없기에 무조건 답은 0
#         num = 0
#         break
#     elif t == 0 or t > 12:
#         min_or_secs += 1
#     else:
#         all += 1
# # 3개를 무조건 시, 분, 초로 1개씩 할당해야 하기 때문에
# # all = 1 인 경우, '시'가 올 수 있는 위치가 1개로 고정됨 -> 나머지 2개가 서로 교환될 수 있으므로 경우의 수: 2
# # all = 2 인 경우, '시'가 될 수 있는 위치가 2곳 x '시' 위치를 제외한 나머지 위치가 서로 교환될 수 있기에 2가지: 2x2 = 4
# # all = 3인 경우, '시'가 될 수 있는 위치가 3곳 -> 3 x 2 x 1 = 6
# # 결국,
# num = all * 2
    
# 위 내용을 정리해보면 결국 아래의 식으로 정리할 수 있음.
# " '시' 가 될 수 있는 위치 x 2 x 1 "
# 그렇기에 '시'가 될 수 있는 경우가 몇 개인지 세고 두 배 해주면 답임.
# ('시'가 될 수 있는 숫자의 범위는 1 <= t <= 12)
# 따라서 아래의 내용으로 간단히 정리

for t in times:
    if t > 59: # 59가 초과되는 숫자가 하나라도 있는 이상 정상적인 시간으로 읽을 수 없기에 무조건 답은 0
        num = 0
        break
    if 1 <= t <= 12:
        num += 2
        
print(num)