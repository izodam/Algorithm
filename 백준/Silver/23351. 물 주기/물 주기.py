def watering(n, k, a, b):
    arr = [k] * n

    day = 0
    while 0 not in arr:

        # A개의 화분에 B씩 물주기
        for i in range(a):
            arr[i] += b

        # 모든 화분의 수분이 1씩 감소
        for i in range(len(arr)):
            arr[i] -= 1

        # 수분이 적은 순으로 재 정렬
        arr.sort()
        day += 1

    return day


n, k, a, b = map(int, input().split())
print(watering(n, k, a, b))