n, m = map(int, input().split())
pokemon_dictonary1 = {}

for i in range(n):
    pokemon_name = input()
    pokemon_dictonary1[pokemon_name] = f'{i+1}'

pokemon_dictonary2 = {v:k for k, v in pokemon_dictonary1.items()}

for j in range(m):
    problem = input()
    if not problem.isnumeric():
        print(pokemon_dictonary1[problem])
    else:
        print(pokemon_dictonary2[problem])