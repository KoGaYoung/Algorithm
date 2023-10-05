import sys
'''
5
2 10 4
1 9 4
2 4 4
2 2 4
1 5 4
202
104
202
202
104
'''
# if __name__ == "__main__":
t = int(sys.stdin.readline())
for _ in range(0, t):
    h, w, n = map(int, sys.stdin.readline().split())

    if n % h == 0:
        print(str(h) + str(int(n/h)).rjust(2, '0'))
    else:
        print(str(n%h) + str(int(n/h)+1).rjust(2,'0'))