# 11501번
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int,input().split()))

    res = 0

    max_number = numbers[-1]

    for i in range(n-2,-1,-1):
        if numbers[i] > max_number:
            max_number = numbers[i]         # 최대값보다 크면 max_number 업데이트

        else:
            res += (max_number - numbers[i])        # 아니면 이득생김 -> 최대값에서 지금 사는 값 뺀만큼!
    print(res)