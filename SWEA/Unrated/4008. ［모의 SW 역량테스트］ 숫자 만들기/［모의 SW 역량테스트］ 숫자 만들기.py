def dfs(i, now):
    global res_min, res_max
    if i == n:
        res_min = min(res_min, now)
        res_max = max(res_max, now)
        return
    if oper[0] > 0:
        oper[0] -= 1
        dfs(i+1, now + number[i])
        oper[0] += 1

    if oper[1] > 0:
        oper[1] -= 1
        dfs(i+1, now - number[i])
        oper[1] += 1

    if oper[2] > 0:
        oper[2] -= 1
        dfs(i+1, now * number[i])
        oper[2] += 1

    if oper[3] > 0:
        oper[3] -= 1
        tmp = now
        if tmp < 0:
            tmp *= -1
            tmp //= number[i]
            tmp *= -1
        else:
            tmp //= number[i]
        dfs(i+1, tmp)
        oper[3] += 1


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # +', '-', '*', '/'
    oper = list(map(int,input().split()))
    number = list(map(int,input().split()))

    res_min = 10e8
    res_max = -10e8

    dfs(1, number[0])

    print(f'#{tc}', res_max - res_min)