# n = min, m = max
n, m = map(int,input().split())
end = int(m ** 0.5)

# min~max까지의 숫자 개수
res = m - n + 1

# 방문 여부 확인
visit = [0] * (res)

# m까지 돌지 않고 m의 루트까지만 돌아도 모든 소수 판정 가능
for i in range(2, end+1):
    # 제곱의 배수를 찾기
    x = i ** 2

    # n부터 봐야하므로 해당 제곱수의 배수부터 시작하기 위한 시작점 찾기
    start = ((n-1) // x + 1) * x

    for j in range(start, m+1, x):
        if not visit[j-n]:
            res -= 1
            visit[j-n] = 1

print(res)