# 약수의 개수가 짝수인 숫자 번째의 창문은 결국 닫힌 상태가 되고
# 약수의 개수가 홀수인 숫자 번째의 창문은 결국 열린 상태가 된다.
# 이에 이어 약수의 개수가 홀수인 숫자는 제곱수이다(ex. 4, 9, 16...)
# 그렇기에 N 이내에 제곱수가 몇 개인지를 세면 그게 답임.

N = int(input())

result = 0

# 시간 초과
# for i in range(N):
#     if i ** 2 <= N:
#         result +=1

x = 1
while x*x <= N:
    x += 1
    result += 1
print(result)

# 또는
# N 이하의 제곱수의 개수는 sqrt(N) 값이므로
# print(int(N ** 0.5))