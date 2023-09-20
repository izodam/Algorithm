import sys
input = sys.stdin.readline
def round4(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

n = int(input())
if n == 0:
    print(0)
else:
    level = [int(input()) for _ in range(n)]
    level.sort()
    #내장함수 round는 오사오입. 현재 필요한 것은 사사오입 -> 새로운 함수 정의
    x = round4(n*0.15)  # 제거할 값 갯수
    res = level[x:-x]
    if x>0:
        print(round4(sum(res)/len(res)))
    else:
        print(round4(sum(level)/len(level)))