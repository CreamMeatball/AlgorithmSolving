# # N과 L을 입력받는다
# N, L = map(int, input().split())

# # len = L부터 N // 2까지 순회
# for len in range(L, N // 2 + 1):
#     # start는 0부터 N까지 순회
#     for start in range(N):
#         # start * len + (len * (len - 1)) // 2는 등차수열의 합을 구하는 공식
#         sumOfNumbers = start * len + (len * (len - 1)) // 2
#         # 만약 합이 N과 같다면
#         if sumOfNumbers == N:
#             # 정답 출력
#             for i in range(start, start + len):
#                 print(i, end=' ')
#             exit(0)
#         # 만약 합이 N보다 크다면
#         if sumOfNumbers > N:
#             # 더 이상 순회할 필요가 없으므로 반복문 이탈.
#             break
#     # 만약 len이 N // 2와 같다면
#     if len == N // 2:
#         # 정답이 없으므로 -1 출력 후 종료
#         print(-1)
#         exit(0)

# 위 코드 시간 초과 남.
        
N, L = map(int, input().split())

found = False

for length in range(L, 101):
    temp = N - (length * (length - 1)) // 2
    if temp < 0:
        break
    if temp % length == 0:
        start = temp // length
        for i in range(start, start + length):
            print(i, end=' ')
        found = True
        break

if not found:
    print(-1)