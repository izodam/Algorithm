import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def postorder(root, end):
    if root > end:
        return
    right = end + 1
    for i in range(root+1, end+1):
        # 오른쪽 서브트리 시작점 찾기
        if arr[root] < arr[i]:
            right = i
            break
    # 왼쪽 서브트리 탐색
    postorder(root+1, right-1)
    # 오른쪽 서브트리 탐색
    postorder(right, end)
    # 출력
    print(arr[root])


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

postorder(0, len(arr) - 1)