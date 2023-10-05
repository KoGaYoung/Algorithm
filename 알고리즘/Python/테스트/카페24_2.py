'''


문제 설명
자신의 국어 수학 영어 3 과목의 시험 성적을 확인했습니다. 평균과 등급을 구할 수 있는 프로그램을 작성하십시오.

평균은 소수점 2 번째 자리까지만(3 번째 자리에서 반올림) 출력하며 등급은 평균 90점 이상일 경우 A, 90점 미만 80점 이상인 경우 B, 80점 미만 70점 이상이 C, 70점 미만 60점 이상이 D이고 60점 미만으로는 F입니다.

점수의 평균은 소수점 2번째 자리까지 표시하며, 리턴값은 모두 String 형식으로 반환합니다.

입력 : 국어 영어 수학 순으로 점수 입력(각 과목 당 100점 만점)

출력 : 평균, 등급

'''


def solution(numArr):
    answer = []
    # 평균
    grade = sum(numArr) / len(numArr)
    answer.append('{:.2f}'.format(grade))

    # 등급
    if 90 <= int(grade):
        answer.append('A')
    elif 80 <= int(grade) < 90:
        answer.append('B')
    elif 70 <= int(grade) < 80:
        answer.append('C')
    elif 60 <= int(grade) < 70:
        answer.append('D')
    else:
        answer.append('F')

    return answer