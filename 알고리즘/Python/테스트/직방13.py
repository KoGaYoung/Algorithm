# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())
total_t = 0
for _ in range(0, t):
    tc = input()
    n = 0

    if tc[-2] == 'k':
        total_t += int((float(tc[:-2]) * 1000) // 100)
    else:
        total_t += int(tc[:-1]) // 100

print(total_t)


'''
입력
5
120g
170g
251g
1.32kg
212g

출력
19


입력
7
1.0kg
1.2kg
140g
117g
302g
199g
719g

출력
35
'''