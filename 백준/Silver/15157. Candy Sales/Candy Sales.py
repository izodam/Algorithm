def cheapest_candy_prices(n, w):
    # 결과를 저장할 리스트 초기화
    result = [0] * n

    # 현재 가장 저렴한 가격을 추적할 변수 초기화
    min_price = float('inf')

    # 각 날마다의 가장 저렴한 가격을 계산
    for day in range(n):
        # 오늘 출시된 사탕의 가격 갱신
        min_price = min(min_price + 1, w[day])
        result[day] = min_price

    return result


n = int(input())
w = list(map(int, input().split()))


result = cheapest_candy_prices(n, w)

print(' '.join(map(str, result)))