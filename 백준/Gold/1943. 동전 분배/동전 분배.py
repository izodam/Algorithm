import sys
input = sys.stdin.readline

for tc in range(3):
    n = int(input())
    coins = []
    total = 0

    for _ in range(n):
        price, cnt = map(int, input().split())
        total += price * cnt
        coins.append([price, cnt])

    # 윤화와 준희는 각각 total / 2 만큼 가져야 반띵임
    if total % 2:
        print(0)
        continue

    total //= 2

    dp = [0] * (total + 1)
    dp[0] = 1

    res = 0

    for price, cnt in coins:
        for n in range(total, price-1, -1):
            if dp[n-price]:
                for j in range(cnt):
                    if n + price * j <= total:
                        dp[n+price*j] = 1
                    else:
                        break
            if dp[-1]:
                res = 1
                break
    print(res)