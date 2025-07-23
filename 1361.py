import sys

S1 = str(input())
S2 = str(input())

S1_LEFT = S1.split('*')[0]
S1_RIGHT = S1.split('*')[1]

S2_LEFT = S2.split('*')[0]
S2_RIGHT = S2.split('*')[1]

# print(f"S1_LEFT: {S1_LEFT}")
# print(f"S1_RIGHT: {S1_RIGHT}")
# print(f"S2_LEFT: {S2_LEFT}")
# print(f"S2_LEFT: {S2_RIGHT}")

# LEFT 만들기
min_len = min(len(S1_LEFT), len(S2_LEFT))
if S1_LEFT[:min_len] != S2_LEFT[:min_len]: # 왼쪽 끝에서부터 비교했을 때, 더 짧은 길이의 LEFT만큼이 완전히 동일함이 보장돼야 함.
    print(-1)
    sys.exit()
RESULT_LEFT = S1_LEFT if len(S1_LEFT) >= len(S2_LEFT) else S2_LEFT
        
# RIGHT 만들기
min_len = min(len(S1_RIGHT), len(S2_RIGHT))
# min_len = 0 일 때 '-0' = '0' 이 돼버려서 오른쪽부터 세는 게 안되므로 주의
if min_len != 0 and S1_RIGHT[-min_len:] != S2_RIGHT[-min_len:]: # 오른쪽 끝에서부터 비교했을 때, 더 짧은 길이의 RIGHT만큼이 완전히 동일함이 보장돼야 함.
    print(-1)
    sys.exit()
RESULT_RIGHT = S1_RIGHT if len(S1_RIGHT) >= len(S2_RIGHT) else S2_RIGHT
        
# 중복 제거 전 결과
# print(RESULT_LEFT + RESULT_RIGHT)        
        
# 중복 제거
# overlap = 0
# for k in range(min(len(RESULT_LEFT), len(RESULT_RIGHT)), -1, -1):
#     if RESULT_LEFT[-k:] == RESULT_RIGHT[:k]:
#         overlap = k
#         break

# answer = RESULT_LEFT + RESULT_RIGHT[overlap:]
# print(answer)

# 위 결과 출력 코드가 아래 반례에서 틀림
# 입력
# A*A
# A*AA

# 정답
# AAA

# 출력
# AA

need_len = max(len(S1_LEFT) + len(S1_RIGHT), len(S2_LEFT) + len(S2_RIGHT))

max_k = min(len(RESULT_LEFT), len(RESULT_RIGHT))
best_k = -1

for k in range(max_k, -1, -1):
    if k == 0 or RESULT_LEFT[-k:] == RESULT_RIGHT[:k]: # 중복 있을 경우
        total_len = len(RESULT_LEFT) + len(RESULT_RIGHT) - k
        if total_len >= need_len: # 길이 조건 만족?
            best_k = k
            break

answer = RESULT_LEFT + RESULT_RIGHT[best_k:]
print(answer)