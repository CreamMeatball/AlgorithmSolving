N = int(input())

people = [list(input()) for _ in range(N)]
 
famous = [[0] * N for _ in range(N)]
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if people[i][j] == "Y" or (people[i][k] == "Y" and people[k][j] == "Y"):
                famous[i][j] = 1
                
result = 0       
for f in famous:
    result = max(result, sum(f))
    
print(result)
            
