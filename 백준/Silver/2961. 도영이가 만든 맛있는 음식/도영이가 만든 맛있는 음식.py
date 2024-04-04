import sys
input = sys.stdin.readline

def back(depth, s, b):
    global res
    if depth == n:
        if s!= 1 and b != 0:
            res = min(res, abs(s-b))
        return

    # 현재 깊이의 재료 추가
    back(depth+1, s*food[depth][0], b+food[depth][1])
    # 추가하지 않고 다음 재료 확인
    back(depth+1, s, b)

n = int(input())

# 신맛은 곱, 쓴맛은 합
food = [list(map(int,input().split())) for _ in range(n)]
res = float('inf')
back(0,1,0)
print(res)