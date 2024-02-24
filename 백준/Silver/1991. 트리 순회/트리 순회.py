# 전위
def preorder(t):
    if t != '.':
        res_pre.append(t)
        preorder(tree[t][0])
        preorder(tree[t][1])

# 중위
def inorder(t):
    if t != '.':
        inorder(tree[t][0])
        res_in.append(t)
        inorder(tree[t][1])

# 후위
def postorder(t):
    if t != '.':
        postorder(tree[t][0])
        postorder(tree[t][1])
        res_pst.append(t)


n = int(input())
tree = {}

# 트리 만들기
for i in range(1,n+1):
    node, l, r = input().split()
    tree[node] = [l,r]

res_pre = []
res_in = []
res_pst = []

preorder('A')
inorder('A')
postorder('A')

print(''.join(res_pre))
print(''.join(res_in))
print(''.join(res_pst))