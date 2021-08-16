import math

def solution(x, y, r, v):
    x_l = []  # x 왼쪽 좌표
    x_r = []  # x 오른쪽 좌표
    y_b = []  # y 아래 좌표
    y_t = []  # y 위 좌표
    for idx in range(0, len(x)):
        x_l.append(x[idx] - r[idx])
        x_r.append(x[idx] + r[idx])
        y_b.append(y[idx] - r[idx])
        y_t.append(y[idx] + r[idx])

    # 직사각형좌표 : 두 원을 포함한 최소 직사각형을 만들려면 l, b는 최소 / r, t는 최대
    r_l = min(x_l)
    r_r = max(x_r)
    r_b = min(y_b)
    r_t = max(y_t)

    # 직사각형 면적
    r_area = (r_r - r_l) * (r_t - r_b)

    coo = []
    # 난수 좌표 셋 만들기
    for i in range(int(len(v)/2)):
        ran_x = v.pop(0)
        ran_y = v.pop(0)

        # x시작+ran_x좌표 % x차이, y시작+ran_y좌표 % y차이
        coo.append((r_l + ran_x % (r_r - r_l), r_b + ran_y % (r_t - r_b)))

    # 난수좌표 원안에 있는지 검사하여 카운트
    incircle_count = 0
    for coo_xy in coo:
        for idx in range(len(x)):  # 두 원중 하나에만 있으면 카운트
            # (반지름 ^ 2) >= (((원의 중심 좌표 x[idx] - 임의의 좌표 coo_xy[0]) ^ 2) + ((원의 중심 좌표 y[idx] - 임의의 좌표 coo_xy[1]) ^ 2)))
            if (math.pow(r[idx], 2) >= (math.pow(x[idx] - coo_xy[0], 2) + math.pow(y[idx] - coo_xy[1], 2))):
                incircle_count += 1
                break

    rate = incircle_count / len(coo)
    answer = int(rate * r_area)
    return answer

print(solution([5], [5], [5], [92, 83, 14, 45, 66, 37, 28, 9, 10, 81]))

print(solution([3, 4], [3, 5], [2, 3], [12, 83, 54, 35, 686, 337, 258, 95, 170, 831, 8, 15]))
