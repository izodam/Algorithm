# 25192번
import sys
input = sys.stdin.readline

n = int(input())
chat = [input().rstrip() for _ in range(n)]

chat_list = {}
res = 0
for user in chat:
    if user == 'ENTER':
        chat_list = {}
    else:
        if user in chat_list:
            continue
        else:
            chat_list[user] = 1
            res += 1

print(res)