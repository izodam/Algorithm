from collections import deque

def cheak_mag(s, n,rotate):
    if 0 <= n+1 < 4 and n+1 not in arr:
        if mag[n][2] != mag[n+1][6]:
            cheak.append((n+1, rotate*(-1)))
            arr.append(n+1)
            cheak_mag(s, n+1,rotate*(-1))

    if 0 <= n-1 < 4 and n-1 not in arr:
        if mag[n-1][2] != mag[n][6]:
            cheak.append((n-1, rotate*(-1)))
            arr.append(n-1)
            cheak_mag(s, n-1,rotate*(-1))

    return

mag = [deque(map(int,input().strip())) for _ in range(4)]
k = int(input())
# N 극이 0 으로, S 극이 1
# 0의 idx 2와 1의 idx 6 붙어있음
# 1의 idx 2와 2의 idx 6 붙어있음
# 2의 idx 2와 3의 idx 6 붙어있음
res = 0

# k번 회전
for _ in range(k):
    # 시계방향이 1, 반시계 방향이 -1
    # 시계방향이 리스트 rotate 1
    # 반시계가 리스트 rotate -1
    n, direction = map(int,input().split())
    # 돌렸을 때 체크해야하는 자석과 방향들 넣어주기
    cheak = [(n-1, direction)]
    # 중복 제거 위해서 리스트 하나 더 만듦...
    arr = [n-1]
    cheak_mag(n-1, n-1, direction)
    # 회전 시작
    for n,direction in cheak:
        mag[n].rotate(direction)

for i in range(4):
    if mag[i][0]:
        res += 2**i
print(res)