A, B, C = map(int, input().split())

# print(A ** B % C)
# ⬆️ 시간 초과 남

# (A에 B를 곱하고 C로 나눠 나온) '나머지에 B를 곱하고' 그걸 C로 나눈 나머지 = A에 B를 곱하고 C로 나눈 나머지
# result = A
# while(B > 1):
#     result *= A
#     result %= C
#     B -= 1
# print(result)
# ⬆️ 이것도 시간 초과 남

# 수학적으로 풀기.
# B가 짝수일 땐     A^B % C = A^(B//2) * A^(B//2) % C
# B가 홀수일 땐     A^B % C = A^(B//2) * A^(B//2) * A % C
# 여기서 A^(B//2) 는 또 A^(B//4) * A^(B//4) 로 또 쪼개는 거임
# 이런 식으로 재귀로 풀면, 연산 횟수가 줄어들음.
# 예를 들어 A^100 (B : 100) 이면, A를 곱하는 연산을 100번 해야되는데
# 재귀로 분할해서 풀면 100 > 50 > 25 > 12 > 6 > 3 > 1
# 총 6번 재귀되고, 각 재귀마다 항이 2배로 늘어나니까
# 2^6 = 64 번으로 연산 횟수가 줄어들음.

def recursive_power(A, B):
    if B == 1:
        return A % C
    else:
        temp = recursive_power(A, B // 2)
        if B % 2 == 0:
            return temp ** 2 % C
        else:
            return temp ** 2 * A % C
        
print(recursive_power(A, B))