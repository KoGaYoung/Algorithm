import sys
# if __name__ == "__main__":
answer = 0
t = int(sys.stdin.readline())
for _ in range(0, t):
    word = sys.stdin.readline()
    memory = []
    old = ''
    flag = True
    for ch in word:
        if ch == old:
            pass
        else:
            if ch in memory:
                flag = False
            else:
                old = ch
                memory.append(ch)
    if flag:
        answer += 1

print(answer)