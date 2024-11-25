import sys
input = sys.stdin.readline

n = int(input())
word = [(input().strip(), i) for i in range(n)]
prefix = ''
min_idx = float('inf')
word.sort()

for i in range(n-1):
    if word[i][0] == word[i+1][0]:
        continue
    maxlen = min(len(word[i][0]), len(word[i+1][0]))
    idx = min(word[i][1], word[i+1][1])
    for j in range(maxlen):
        if word[i][0][j] != word[i+1][0][j]:
            break
        if j == maxlen - 1:
            j += 1
    if len(prefix) < j or len(prefix) == j and idx < min_idx:
        prefix = word[i][0][:j]
        min_idx = idx

res = []
for w, i in word:
    if w[:len(prefix)] == prefix:
        res.append((w, i))
res.sort(key=lambda x:x[1])
for i in res[:2]:
    print(i[0])