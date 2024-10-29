import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
words = defaultdict(int)

for _ in range(n):
    word = input().strip()
    x = len(word) - 1
    for alpha in word:
        words[alpha] += 10 ** x
        x -= 1

sorted_words = sorted(words.values(), reverse=True)

res = 0
number = 9
for cnt in sorted_words:
    res += number * cnt
    number -= 1
print(res)