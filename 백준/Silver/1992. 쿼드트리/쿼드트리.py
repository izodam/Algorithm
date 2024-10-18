import sys
sys.setrecursionlimit(10**6)
n = int(input())
board = [list(map(int,input())) for _ in range(n)]

def quadtree(n, video):
    check = 0
    for i in video:
        check += sum(i)

    if check == n ** 2:
        return '1'
    if check == 0:
        return '0'

    half = n // 2
    tmp = '('
    tmp += quadtree(half, [s[:half] for s in video[:half]])
    tmp += quadtree(half, [s[half:] for s in video[:half]])
    tmp += quadtree(half, [s[:half] for s in video[half:]])
    tmp += quadtree(half, [s[half:] for s in video[half:]])
    tmp += ')'

    return tmp
print(quadtree(n, board))