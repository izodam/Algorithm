import sys
input = sys.stdin.readline


def push(li,x):
    li.append(x)
def pop(li):
    if len(li)==0:
        print(-1)
    else:
        print(li[-1])
        li.pop()
def size(li):
    print(len(li))
def empty(li):
    if len(li)==0:
        print(1)
    else:
        print(0)
def top(li):
    if len(li) == 0:
        print(-1)
    else:
        print(li[-1])

n=int(input())
stack=[]
for i in range(n):
    commend=input().split()
    if commend[0]=='push':
        push(stack,commend[1])
    if commend[0]=='pop':
        pop(stack)
    if commend[0]=='size':
        size(stack)
    if commend[0]=='empty':
        empty(stack)
    if commend[0]=='top':
        top(stack)