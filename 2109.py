import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

# 처음에 (d, -p) 로 최소 힙 넣는 방식으로 구현했는데
# 아래와 같은 반례에서 틀리게 됨.
# 강연료 (p)	마감일 (d)
# 10          1
# 100	      2
# 50	      2


# (day, pay) 기준으로 heapq 를 쓰면 day가 앞설 경우 pay가 낮아도 포함해버리는 문제가 생기고
# (pay, day) 기준으로 하면 더 비싼 pay를 먼저 하느라 앞선 day의 괜찮은 pay의 강의를 날려버리고 다음 day로 진입해서 오히려 수익이 적어지는 문제가 생김

# 그래서 둘 다 고려하는 법을 고안

lectures = []
for _ in range(n):
    p, d = map(int, input().rstrip().split())
    lectures.append((d, p)) # (마감일, 강연료) 순서로 저장

# 마감일을 기준으로 오름차순 정렬. 일단 day 우선으로 request를 탐색하기 위함.
lectures.sort()

# 강연료만 저장할 최소 힙 (가장 낮은 강연료를 쉽게 빼기 위함)
candidate_pays = []

for d, p in lectures: # 전제: lectures.sort() (day 기준 정렬)
    # 일단 후보 힙에 현재 강연의 강연료를 추가 (적은 강연료가 앞에 오게끔)
    heapq.heappush(candidate_pays, p)
    
    # d일 동안 할 수 있는 강의 수를 초과했다면
    if len(candidate_pays) > d:
        # 힙에서 가장 작은 값(가장 낮은 강연료)을 제거
        # 이 과정에서 앞선 날의 강연료가 낮은 것들을 제거하게 됨.
        heapq.heappop(candidate_pays)
        
print(sum(candidate_pays))