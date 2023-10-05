import sys
t = int(sys.stdin.readline())
for _ in range(0, t):
    n = int(sys.stdin.readline())

    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    applicants.sort(key=lambda x: (x[0]))

    answer = 1
    m = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < m:
            answer += 1
            m = applicants[i][1]

    print(answer)
    # flag = [1 for _ in range(n)]
    #
    # for i in range(0, n):
    #     if flag[i] == 1:
    #         m = applicants[i][1]
    #         for j in range(i + 1, n):
    #             if m < applicants[j][1]:
    #                 flag[j] = 0
    #
    # print(sum(flag))

