import sys

a = int(sys.stdin.readline())
origin = list(map(int, sys.stdin.readline().split()))
origin.sort()
b = int(sys.stdin.readline())
verif = list(map(int, sys.stdin.readline().split()))

for find in verif:
    left = 0
    right = len(origin) - 1

    found = False
    while True:
        # mid = int(len(origin)/2)-1 if len(origin) % 2 == 0 else int(len(origin)/2)
        mid = (left + right) // 2

        if find == origin[mid]:
            print(1)
            found = True
            break
        elif find > origin[mid]:
            left = mid + 1
        elif find < origin[mid]:
            right = mid - 1

        if right < left:
            break

    if not found:
        print(0)

