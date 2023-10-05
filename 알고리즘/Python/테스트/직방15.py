# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 첫번 째 계단에는 서 있기 때문에 2<=K 아닌가요?
import math

k, n = map(int, input().split())
s = list(map(int, input().split()))

need_k = 0
total_n = s[0]
for i in range(1, n):
    need_k += s[i] - total_n
    total_n = s[i]

print(math.ceil(need_k / k))

'''
입력
2 5
1 3 5 7 9

출력
4

입력
2 5
1 3 5 7 12

출력
6
'''