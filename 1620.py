N, M = map(int, input().split())

pokemon_dict = {}
for i in range(1, N+1):
    pokemon = input()
    pokemon_dict[i] = pokemon
    pokemon_dict[pokemon] = i
    # pokemon_dict[i] = pokemon 만 저장해놓으면, 나중에 value를 통해 key 값을 찾을 때 전체를 다 순환해서 찾아야되는 시간 문제가 생김.
    
for i in range(M):
    question = input()
    # if isinstance(question, int):
    # 위 코드는 input() 이 항상 str을 반환해서 작동이 안됨
    if question.isdigit():
        print(pokemon_dict[int(question)])
    else:
        print(pokemon_dict[str(question)])