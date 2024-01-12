n, m =map(int,input().split())
num = list(map(int,input().split()))
num.sort()      # 사전 순으로 증가하며 출력되기 위해 받은 숫자들 정렬
ans = []

def back():
    if len(ans) == m:
        print(' '.join(map(str,ans)))   # 수열이 m개이면 출력!
        return
    for i in num:
        ans.append(i)
        back()
        ans.pop()   # 리스트의 가장 마지막 요소 빼고 다음 요소 넣기위해

back()