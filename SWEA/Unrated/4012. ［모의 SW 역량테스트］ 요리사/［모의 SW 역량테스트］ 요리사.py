def findsum(arr):
    food1 = arr[:]
    food2 = [i for i in range(n) if i not in arr]

    res1 = 0
    res2 = 0

    for i in range(len(food1) - 1):
        for j in range(i+1, len(food1)):
            res1 += board[food1[i]][food1[j]] + board[food1[j]][food1[i]]
            res2 += board[food2[i]][food2[j]] + board[food2[j]][food2[i]]

    return abs(res1-res2)


def dfs(a, x):
    global res
    if x == n // 2:
        now = findsum(arr)
        res = min(res, now)
        return
    for i in range(a, n):
        arr.append(i)
        dfs(i+1, x+1)
        arr.pop()



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # n개의 음식을 두개로 나누기
    board = [list(map(int,input().split())) for _ in range(n)]
    arr = []
    res = 10e10
    dfs(0,0)
    print(f'#{tc}',res)
