N, M = map(int, input().split())

didnt_listen = set()
didnt_see = set()
didnt_listen_see = set()

for i in range(N):
    didnt_listen.add(input())
    
for i in range(M):
    input_data = input()
    didnt_see.add(input_data)
    if input_data in didnt_listen:
        didnt_listen_see.add(input_data)
        
print(len(didnt_listen_see))
for name in sorted(didnt_listen_see):
    print(name)