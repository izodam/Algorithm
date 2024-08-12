t = int(input())

for tc in range(t):
    n = int(input())
    prison = [False] * (n+1)
    for round in range(1, n+1):
        for i in range(round, n+1, round):
            prison[i] = not prison[i]

    print(prison.count(True))