# 1744번
n = int(input())
nums = [int(input()) for _ in range(n)]

plus = []
minus = []
res = 0

for i in nums:
    # 1 보다 크면 plus에
    if i > 1:
        plus.append(i)
    # 0보다 같거나 작으면(음수) minus에
    elif i <= 0:
        minus.append(i)
    # 1이면 그냥 더하기 -> 묶지 않고 더하는게 제일 크므로
    else:
        res += i

# 양수는 큰 수끼리 묶는게 가장 큼
plus.sort(reverse=True)
# 음수는 작은 수끼리 묶는게 가장 큼 (-)*(-)는 (+)이기 때문
minus.sort()

# 양수 묶기
for i in range(0,len(plus),2):
    # 마지막 수
    if i+1 >= len(plus):
        res += plus[i]
    else:
        res += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0,len(minus),2):
    if i+1 >= len(minus):
        res += minus[i]
    else:
        res += (minus[i] * minus[i+1])

print(res)