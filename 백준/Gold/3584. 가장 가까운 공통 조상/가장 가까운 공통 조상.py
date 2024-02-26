import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    par = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        par[b] = a

    node1, node2 = map(int,input().split())

    par_node1 = []
    par_node2 = []

    while par[node1] != 0:
        par_node1.append(node1)
        node1 = par[node1]
    while par[node2] != 0:
        par_node2.append(node2)
        node2 = par[node2]
    par_node1.append(node1)
    par_node2.append(node2)

    for i in par_node1:
        if i in par_node2:
            print(i)
            break