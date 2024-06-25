# 14889. 스타트와 링크
import sys
input = sys.stdin.readline

def findsum(arr):
    start = arr[:]
    link = [i for i in range(n) if i not in arr]

    res1 = 0
    res2 = 0

    for i in range(len(start)-1):
        for j in range(i+1, len(start)):
            res1 += board[start[i]][start[j]] + board[start[j]][start[i]]
            res2 += board[link[i]][link[j]] + board[link[j]][link[i]]
    return abs(res1-res2)

def back(a, x):
    global res
    if x == n // 2:
        now = findsum(arr)
        res = min(res, now)
        return
    for i in range(a, n):
        arr.append(i)
        back(i+1, x+1)
        arr.pop()

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
arr = []
res = float('inf')
back(0, 0)
print(res)