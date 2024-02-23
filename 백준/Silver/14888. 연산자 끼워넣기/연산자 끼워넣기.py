# 14888
n = int(input())
a = list(map(int, input().split()))
# +, -, *, // 순
oper = list(map(int, input().split()))

res_min = 10e10
res_max = -10e10

def dfs(i, now):
    global res_max, res_min
    if i == n:
        res_min = min(res_min, now)
        res_max = max(res_max, now)
        return
    if oper[0] > 0:
        oper[0] -= 1
        dfs(i+1, now + a[i])
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        dfs(i + 1, now - a[i])
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        dfs(i + 1, now * a[i])
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        if now < 0:
            now *= -1
            now //= a[i]
            now *= -1
        else:
            now //= a[i]
        dfs(i + 1, now)
        oper[3] += 1

dfs(1, a[0])

print(res_max)
print(res_min)