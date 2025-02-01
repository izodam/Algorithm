import sys
input = sys.stdin.readline
import sys
input = sys.stdin.readline
# 배열 a, b를 합한 모든 경우의 수와
# 배열 c, d를 합한 모든 경우의 수를 가지고 투포인터 사용하여 0 찾기
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

sumAB = []
sumCD = []

for i in range(n):
    for j in range(n):
        sumAB.append(arr[i][0] + arr[j][1])
        sumCD.append(arr[i][2] + arr[j][3])

sumAB.sort()
sumCD.sort()

res = 0
left = 0
right = len(sumCD) - 1

while right >= 0 and left < len(sumCD):
    now = sumAB[left] + sumCD[right]

    if now < 0:
        left += 1
    elif now > 0:
        right -= 1

    else:
        ab = 1
        # sumAB에서 같은 값의 개수
        i = left + 1
        while i < len(sumAB) and sumAB[i] == sumAB[left]:
            ab += 1
            i += 1

        cd = 1
        # sumCD에서 같은 값의 개수
        i = right - 1
        while i >= 0 and sumCD[i] == sumCD[right]:
            cd += 1
            i -= 1

        res += ab * cd
        left += ab
        right -= cd



print(res)