course = []

for i in range(20):
    course.append(list(map(str, input().split())))

scoresum = 0
coursesum = 0

# print(course)

for i in range(20):
    if course[i][2] == 'P':
        continue
    else:
        if course[i][2] == 'A+':
            scoresum += float(course[i][1])*4.5
        elif course[i][2] == 'A0':
            scoresum += float(course[i][1])*4.0
        elif course[i][2] == 'B+':
            scoresum += float(course[i][1])*3.5
        elif course[i][2] == 'B0':
            scoresum += float(course[i][1])*3.0
        elif course[i][2] == 'C+':
            scoresum += float(course[i][1])*2.5
        elif course[i][2] == 'C0':
            scoresum += float(course[i][1])*2.0
        elif course[i][2] == 'D+':
            scoresum += float(course[i][1])*1.5
        elif course[i][2] == 'D0':
            scoresum += float(course[i][1])*1.0
        elif course[i][2] == 'F':
            scoresum += float(course[i][1])*0.0
            
        coursesum += float(course[i][1])
        
print(f"{scoresum/coursesum:.6f}")