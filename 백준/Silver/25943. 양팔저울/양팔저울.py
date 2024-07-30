import sys

input = sys.stdin.readline

W = [100, 50, 20, 10, 5, 2, 1]  # 무게추 리스트

N = int(input())
P = list(map(int, input().split()))
left, right = P[0], P[1]  # 0번째(왼쪽), 1번째(오른쪽)

for i in range(2, N):
    if left == right:  # 같으면
        left += P[i]  # 왼쪽에 더해줌
    else:  # 그렇지 않으면 작은 쪽에 더해줌
        if left < right:
            left += P[i]
        elif left > right:
            right += P[i]

tmp = abs(left - right)  # 왼쪽과 오른쪽의 차이

if tmp == 0:  # 0이면 0출력
    print(0)
else:  # 아니라면 for문 순회
    cnt = 0  # 무게추 개수 저장할 변수
    for w in W:
        if (tmp // w) != 0:
            cnt += tmp // w  # 몫을 통해 개수 더함
            tmp = tmp % w  # 나머지 초기화
    print(cnt)
