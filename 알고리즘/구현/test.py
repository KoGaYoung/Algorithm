import sys
if __name__ == "__main__":
    a = int(sys.stdin.readline())
    li = []
    for _ in range(a):
        li.append(int(sys.stdin.readline()))
    li.sort()
    for i in li:
        print(i)
    # b = int(sys.stdin.readline())
    # a, b = map(int, sys.stdin.readline().split())
    # print(a//b)
    # print(a%b)
