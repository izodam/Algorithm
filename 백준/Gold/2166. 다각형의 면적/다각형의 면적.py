# 2166
n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]
# 리스트의 마지막에 첫 꼭지점 좌표 하나 더 추가
point.append(point[0])

# 각 꼭지점의 x좌표를 다음 꼭지점 y와 곱해서 더하기
# 각 꼭지점의 y좌표를 다음 꼭지점의 x와 곱해서 더하기
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += point[i][0] * point[i+1][1]
    sum2 += point[i][1] * point[i+1][0]
print(round(abs(sum1 - sum2) / 2,2))