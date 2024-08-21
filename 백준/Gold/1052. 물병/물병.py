n, k = map(int,input().split())
cnt = 0

while bin(n).count('1') > k:
    # 뒤에서부터 1이 가장 먼저 나오는 위치 만큼씩 더해가면 된다
    idx = bin(n)[::-1].index('1')
    cnt += 2 ** idx
    n += 2 ** idx

print(cnt)