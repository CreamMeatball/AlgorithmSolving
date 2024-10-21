def isPrime(number):
    # sqrt(N) 까지만 약수 확인해도 소수 판별이 가능하다고 함.
    # N의 약수들의 중간값이 sqrt(N) 부근이기 때문에.
    
    # 다만 아래 for 구조에서 0, 1을 True(소수라고 판단)로 출력하기 때문에, 이를 보완하기 위해 if문 하나 추가해야함.
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        # 참고) number가 0일 떄는 int(number ** 0.5) 가 0, number가 1,2,3일 때는 int(number ** 0.5) 가 1이 나옴(내림 처리)
        # 그래서 0,1,2,3 까지는 for 문이 아예 시작도 안 함. for i in range(2,2) 이런 식이면 반복문 시작이 안 됨.
        if number % i == 0:
            # print(f"{number} is not a prime")
            return False
    return True

N = int(input())

for i in range(N):
    start_number = int(input())
    # 4*10^10 까지 확인
    for j in range(start_number, 4*10**10+1):
        if isPrime(j):
            print(j)
            break
    # j = start_number
    # while True:
    #     if isPrime(j):
    #         print(j)
    #         break
    #     j += 1