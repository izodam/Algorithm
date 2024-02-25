import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def pre(instart, inend, poststart, postend):
    if (instart > inend) or (poststart > postend):
        return
    root = postorder[postend]

    # 해당 루트의 왼쪽 서브트리 노드 개수
    left = idx[root] - instart
    # 오른족 서브트리 노드 개수
    right = inend - idx[root]

    print(root, end=' ')
    pre(instart, instart+left-1, poststart, poststart+left-1)
    pre(inend - right + 1, inend, postend - right, postend - 1)



n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

root = postorder[-1]
# 중위순회 한 결과의 각 인덱스를 구하기 위함
idx = [0] * (n + 1)
for i in range(n):
    idx[inorder[i]] = i

pre(0, n-1, 0, n-1)