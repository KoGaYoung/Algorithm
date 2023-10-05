import sys

# 동적 개념 적용해보자
if __name__ == "__main__":
    t = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for i in range(t)]
    a_max = max(a)
    zero = [1, 0]
    one = [0, 1]
    for idx in range(2, a_max+1):
        zero.append(zero[idx-2] + zero[idx-1])
        one.append(one[idx - 2] + one[idx - 1])

    for a_item in a:
        print(str(zero[a_item]) + ' ' + str(one[a_item]))