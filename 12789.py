import sys

N = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# print(students)

another_line = [N+1]
accept = [0]

result = "Nice"

# 한 명씩만 설 수 있는 공간에서도, 맨 앞 사람이 자기 순번일 경우 간식 받는 곳으로 빠져나갈 수 있음.
while(students):
    student = students[0]
    # print(f"{student} turn")
    if student == (accept[-1] + 1):
        # print(f"{student} push into accept line")
        accept.append(student)
        students.pop(0)
    elif another_line[-1] == (accept[-1] + 1):
        # print(f"{another_line[-1]} push into accept line")
        accept.append(another_line.pop())
    elif student < another_line[-1]:
        # print(f"{student} push into another line")
        another_line.append(student)
        students.pop(0)
    else:
        result = "Sad"
        break

# print(another_line)
# print(accept)

print(result)