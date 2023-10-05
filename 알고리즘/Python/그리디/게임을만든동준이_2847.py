
import sys


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    level = list(int(input()) for _ in range(t))
    sub_score = 0

    level_max_score = level[len(level)-1]
    for i in range(len(level)-2, -1, -1):
        while level[i] >= level_max_score:
            level[i] -= 1
            sub_score += 1
        level_max_score = level[i]

    print(sub_score)