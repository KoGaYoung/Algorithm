import sys

t = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
a = [1 for _ in range(t)]
for idx, item in enumerate(p):
    big_count = 0
    for com_idx, com_item in enumerate(p):
        if idx != com_idx:
            if item[0] < com_item[0] and item[1] < com_item[1]:
                a[idx] += 1

print(' '.join(str(x) for x in a))