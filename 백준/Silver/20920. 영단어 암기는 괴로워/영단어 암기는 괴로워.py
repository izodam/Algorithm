# 20920
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
word_list = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue
    else:
        # 개수 세서 딕셔너리 저장
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

res = sorted(word_list.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in res:
    print(i[0])