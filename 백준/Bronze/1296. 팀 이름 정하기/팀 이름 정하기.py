yeon = input()
n = int(input())
team = [input() for _ in range(n)]
team.sort()

score = {}

for i in team:
    L = yeon.count('L') + i.count('L')
    O = yeon.count('O') + i.count('O')
    V = yeon.count('V') + i.count('V')
    E = yeon.count('E') + i.count('E')

    win = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if win in score:
        score[win] = min(i, score[win])
    else:
        score[win] = i

print(score[max(score.keys())])