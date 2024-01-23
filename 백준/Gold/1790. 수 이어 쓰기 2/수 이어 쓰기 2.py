# 1790번
n, k = map(int,input().split())

ans = 0
digit = 1       # 자리수 갯수
nine = 9        # 해당 digit을 가지는 숫자 갯수

while k > digit * nine:
    k = k - (digit * nine)
    ans += nine

    digit += 1
    nine *= 10
ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])