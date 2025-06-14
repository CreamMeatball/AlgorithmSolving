import sys
sys.setrecursionlimit(10**6)
input_ = sys.stdin.readline

N = int(input_().strip())

# 문제에서 0은 0번째 감소하는 수이므로 미리 포함한다.
desc_nums = [0]

def dfs(num):
    # 현재 num의 마지막 자릿수보다 아래의 숫자만 붙일 수 있다.
    last = num % 10
    for d in range(last):
        new_num = num * 10 + d
        desc_nums.append(new_num)
        # print(new_num)
        dfs(new_num)
        # 위 dfs가 끝나고 이 줄로 돌아오게 되면(backtracking) 다시 num 값으로 복귀된 상태임.
    # ex)
    # 90 -> 91 -> 910 -> 92 -> 921 -> 9210 -> 93 -> ...

# 1부터 9까지를 시작점으로 DFS 호출
for i in range(1, 10):
    # 위 방식이 한 자리 숫자는 안됨. '앞자리 숫자보다 작은 걸 더한다'라는 방식인데, 한 자리 숫자는 앞자리 숫자가 없으니까.
    # 그래서 한 자리 숫자 0 ~ 9, 총 10개는 직접 넣어줘야 됨.
    desc_nums.append(i)
    dfs(i)
# N이 100만 정도고, 메모리 제한이 커서 다 저장해도 괜찮은 듯

desc_nums.sort()

if N >= len(desc_nums):
    print(-1)
else:
    print(desc_nums[N])