from itertools import permutations


def put(idx, left, right, turn):
    global res
    if idx == n:
        res += 1
        return

    # 왼쪽에 전체 무게의 절반보다 크게 놓았다면
    # 나머지는 오/왼 어디에 놓던 상관이 없음
    if left > weight // 2:
        res += 2 ** (n-idx)
        return

    # 해당 추 왼쪽에 놓기
    put(idx+1, left + turn[idx], right, turn)
    # 오른쪽에 놓기
    if right + turn[idx] <= left:
        put(idx+1, left, right+turn[idx], turn)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 오늘쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가있는 무게의 총합보다 작아야함
    stone = list(map(int,input().split()))

    weight = sum(stone)

    res = 0

    for turn in permutations(stone, n):
        put(0,0,0,turn)
    print(f'#{tc}',res)