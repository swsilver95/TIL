import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemons = {}
pokemons_list = [0]

for i in range(1, N + 1):
    pokemon = input().rstrip()
    pokemons[pokemon] = i
    pokemons_list.append(pokemon)

for _ in range(M):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(pokemons_list[int(tmp)])
    else:
        print(pokemons[tmp])
