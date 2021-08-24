import sys
'''
15
0 15
20 23
0 2147483647
1 2147483647
2 2147483647
41706 2147483647
41707 2147483647
2147483643 2147483647
2147483644 2147483647
2147483645 2147483647
2147483646 2147483647
0 1
0 2
0 3
0 4


7
3
92681
92681
92681
92681
92680
3
3
2
1
1
2
3
3
'''
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance:
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0:  # 짝수일때만 이동거리 늘려줌(앞뒤로 이동하기때문)
            move += 1
    print(count)
