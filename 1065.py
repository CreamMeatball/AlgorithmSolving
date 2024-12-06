def hansu(N) :
    count = 0
    for i in range(1, N+1):
        # 숫자를 분해해서 리스트로 만듦
        num_list = list(map(int,str(i)))
        if i < 100:
            count += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            count += 1
        # 1000의 경우를 따로 필터링 해 줄 필요 없음
        # 위 elif 조건문으로 애초에 걸러짐
    return count

N = int(input())
print(hansu(N))