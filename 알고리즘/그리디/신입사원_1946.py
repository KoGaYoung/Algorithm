# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
t = int(input())
for _ in range(0, t):
    n = int(input())

    applicants = []
    for _ in range(n):
        applicants.append(list(map(int, input().split())))

    # print(applicants)
    applicants.sort(key=lambda x: (x[0], x[1]))
    # print(applicants)
    flag = [True for x in range(0, n)]

    for i in range(0, n):
        if flag[i]:
            m = applicants[i][1]
            for j in range(i + 1, n):
                if m < applicants[j][1]:
                    flag[j] = False
        else:
            pass

    count = 0
    for i in flag:
        if i:
            count += 1
    print(count)
    # print(flag)

