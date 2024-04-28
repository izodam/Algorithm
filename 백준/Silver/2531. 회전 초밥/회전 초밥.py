# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi + sushi
# print(sushi)

res = 0
for i in range(n):
    eat = set(sushi[i:i+k])
    eat.add(c)
    tmp = len(eat)
    res = max(res, tmp)

print(res)