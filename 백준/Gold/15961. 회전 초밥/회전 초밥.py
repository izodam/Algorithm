# 15961. 회전 초밥
# k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
import sys
input = sys.stdin.readline

# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int,input().split())
shi = [int(input()) for _ in range(n)]

# 그룹의 초밥 개수 저장
s = [0] * (d+1)

# 쿠폰 초밥은 무조건 먹음!!
s[c] = 1
# 서로 다른 초밥의 개수
cnt = 1

# 첫 그룹인 k개 접시 선택
for i in range(k):
    s[shi[i]] += 1
    # 해당 초밥이 1개면 개수 추가
    if s[shi[i]] == 1:
        cnt += 1

res = cnt
for i in range(n-1):
    # 슬라이딩
    s[shi[i]] -= 1
    if s[shi[i]] == 0:
        cnt -= 1
    s[shi[(i+k)%n]] += 1
    if s[shi[(i+k)%n]] == 1:
        cnt += 1
    res = max(cnt, res)

print(res)
