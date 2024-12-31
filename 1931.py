import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
meeting = []
for _ in range(N):
    start, end = map(int, input_data().split())
    meeting.append((start, end))
    
# 생각해보면, 끝나는 시간이 빠른 순서대로 정렬하고
# 회의 시작 시간이 이전 회의가 끝나는 시간과 겹치지 않는 것부터 Greedy하게 넣으면,
# 그게 최적이 됨.
# 왜냐면 끝나는 시간이 빠르다는 건,
# 앞선 회의가 끝난 이후에 회의를 시작했을 때 가장 짧게 회의가 진행된다는 것과 같은 의미가 되기 때문에.
    
sorted_meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
# print(sorted_meeting)

meeting_list = [sorted_meeting[0]]

for i in range(1, N):
    if sorted_meeting[i][0] >= meeting_list[-1][1]:
        meeting_list.append(sorted_meeting[i])    
        
# print(meeting_list)
print(len(meeting_list))