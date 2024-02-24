# 전위
def preorder(t):
    if t:
        res_pre.append(tree[t])
        preorder(tree.index(left[t]))
        preorder(tree.index(right[t]))


# 중위
def inorder(t):
    if t:
        inorder(tree.index(left[t]))
        res_in.append(tree[t])
        inorder(tree.index(right[t]))

# 후위
def postorder(t):
    if t:
        postorder(tree.index(left[t]))
        postorder(tree.index(right[t]))
        res_pst.append(tree[t])



n = int(input())

tree =  [0] * (n+1)
left = [0] * (n+1)
right = [0] * (n+1)

root = 0

# 트리 만들기
for i in range(1,n+1):
    node, l, r = input().split()
    tree[i] = node
    if l != '.':
        left[i] = l
    if r != '.':
        right[i] = r
    if node == 'A':
        root = i

res_pre = []
res_in = []
res_pst = []

preorder(root)
inorder(root)
postorder(root)


print(''.join(res_pre))
print(''.join(res_in))
print(''.join(res_pst))