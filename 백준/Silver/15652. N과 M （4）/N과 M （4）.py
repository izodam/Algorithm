n, m =map(int,input().split())
ans = []

def back(x):
    if len(ans) == m:
        print(' '.join(map(str,ans)))   # 수열이 m개이면 출력!
        return
    for i in range(x,n+1):
        ans.append(i)
        back(i)
        ans.pop()   # 리스트의 가장 마지막 요소 빼고 다음 요소 넣기위해

back(1)