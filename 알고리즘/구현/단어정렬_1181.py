import sys

t = int(sys.stdin.readline())
words = []
for i in range(t):
    words.append(sys.stdin.readline().strip())

set_lst = set(words)
words = list(set_lst)
words.sort()
words.sort(key=len)

for i in words:
    print(i)