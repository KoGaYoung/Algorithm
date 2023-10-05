import sys
# if __name__ == "__main__":
'''
1  2  6  7  15
3  5  8  14
4  9  13
10 12
11
1/1  1/2  1/3  1/4  1/5
2/1  2/2  2/3  2/4
3/1  3/2  3/3
4/1  4/2
5/1

대각선으로 보면 첫번째줄 1, 두번째줄2, 세번째줄 3개
대각선기준 분모가 왼쪽에서부터 1 -> 5
        분자가 왼쪽에서부터 5 -> 1
'''
n = int(sys.stdin.readline())
# 몇번 째 라인에 속해있는지 구하기
t = n
i = 1
line = 1
while t - i > 0:
    t -= i
    line += 1
    i += 1
# 해당 라인의 첫번째 숫자 구하기
min_line = 1
for idx in range(line-1):
    min_line += idx+1
# 해당 라인의 첫번째 수로부터 떨어진 거리
baby = 1
parent = line
for _ in range(n - min_line):
    baby += 1
    parent -= 1107
if line % 2 == 0:
    print(str(baby) + '/' + str(parent))
else:
    print(str(parent) + '/' + str(baby))
