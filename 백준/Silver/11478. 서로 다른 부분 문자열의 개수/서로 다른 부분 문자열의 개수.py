s = input()
word = set()
n = len(s)
for i in range(n):
    for j in range(i,n):
        word.add(s[i:j+1])

print(len(word))