import sys
input = sys.stdin.readline

n = int(input())
lope = [int(input()) for _ in range(n)]

'''
만약 lope = [27, 23, 15, 11, 3]이라면
로프를 1개만 사용한다면 버틸 수 있는 최대 중량은 27 * 1 = 27
      2개                                 23 * 2 = 46
      3개                                 15 * 3 = 45
      4개                                 11 * 4 = 44
      5개                                  3 * 5 = 15
이므로, 출력되는 답은 46이다.
'''

# 로프를 큰 순서대로 정렬
lope.sort(reverse=True)

res = []

for i in range(n):
    res.append(lope[i] * (i+1))

print(max(res))