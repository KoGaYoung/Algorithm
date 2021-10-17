# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, m = map(int,input().split())
c = list(map(int, input().split()))
g = list(map(int, input().split()))

c.sort(reverse=True)
g.sort(reverse=True)

while g:
	if c[0] >= g[0]:
		del c[0]
	del g[0]

if not c:
	print('YES')
else:
	print('NO')

'''
입력
5 6
5 3 2 4 1
4 1 4 1 4 1

출력
YES

입력
5 6
5 3 2 4 1
4 1 4 4 1 4


출력
NO
'''