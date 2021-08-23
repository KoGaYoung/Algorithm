def solution(grades):
    # 점수비교할 테이블 만들기
    grade_to_score = {'A+': 12, 'A0': 11, 'A-': 10, 'B+': 9, 'B0': 8, 'B-': 7,'C+': 6,
                      'C0': 5, 'C-': 4, 'D+': 3, 'D0': 2, 'D-': 1, 'F': 0}
    score_to_grade = {}  # {12: 'A+', 11: 'A0', ... , 0: 'F'}
    v = grade_to_score.values()
    k = grade_to_score.keys()
    for x, y in zip(v, k):
        score_to_grade[x] = y

    # 중복제거, 중복일경우 최고점만
    class_grade = {}
    for item in grades:
        item_list = item.split()
        if item_list[0] not in class_grade:
            class_grade[item_list[0]] = grade_to_score[item_list[1]]
        else:
            if class_grade[item_list[0]] < grade_to_score[item_list[1]]:
                class_grade.pop(item_list[0], None)
                class_grade[item_list[0]] = grade_to_score[item_list[1]]
    # 점수로 오름차

    sort_class_grade = sorted(class_grade.items(), key=lambda x: x[1], reverse=True)


    answer = []
    for i in sort_class_grade:
        answer.append(i[0] + ' ' +score_to_grade[i[1]])

    return answer



# print(solution(["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"]))

print(solution(["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]))