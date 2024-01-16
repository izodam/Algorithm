# 15664번
n, m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()      # 사전 순으로 증가하며 출력되기 위해 받은 숫자들 정렬
ans = []

visited = [False] * n   # 방문 여부 확인하기 위한 리스트 생성


def back(x):
    if len(ans) == m:
        print(' '.join(map(str,ans)))   # 수열이 m개이면 출력!
        return

    prev = 0
    for i in range(x,n):
        if visited[i] == False and num[i] != prev:
            visited[i] = True  # 방문 함을 의미
            ans.append(num[i])
            prev = num[i]       # 지금 값 저장


            back(i+1)
            visited[i] = False
            ans.pop()

back(0)