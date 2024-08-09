N = int(input())

i = 0
while(N):
    # 연속되는 666 이기에, string으로 변환 후 '666'이 있는지 확인
    i += 1
    if '666' in str(i):
        N -= 1
    if N == 0:
        print(i)
        break