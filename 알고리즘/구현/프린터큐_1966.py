import sys
'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        imp = list(map(int, input().split()))
        idx = list(range(len(imp)))
        idx[m] = 'target'

        # 순서
        order = 0

        while True:
            # 첫번째 if: imp의 첫번째 값 = 최댓값?
            if imp[0] == max(imp):
                order += 1

                # 두번째 if: idx의 첫 번째 값 = "target"?
                if idx[0] == 'target':
                    print(order)
                    break
                else:
                    imp.pop(0)
                    idx.pop(0)

            else:
                imp.append(imp.pop(0))
                idx.append(idx.pop(0))
