def solution(inp_str):
    answer = []
    ''' 비밀번호 입력규칙중 위배된 규칙번호 담아서 정렬해서 리턴 '''
    # 1
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)
    # 2
    second_con = [False, False, False, False]
    for ch in inp_str:
        if ch.isalpha():       # 알파벳인경우
            if ch.isupper():    # 대문자인경우
                second_con[0] = True
            else:               # 소문자인경우
                second_con[1] = True
        elif ch.isdigit():      # 숫자인경우
            second_con[2] = True
        elif ch in ('~!@#$^&*'):# 특수문자인경우
            second_con[3] = True
        else:
            answer.append(2)
    # 3
    third_con = 0
    for item in second_con:
        if item:
            third_con += 1
    if third_con < 3:
        answer.append(3)
    # 4 and 5
    # 위에 반복문에 한번에 처리할 수 있지만 가독성이 안좋아서 반복문 한번 더돌림
    include = inp_str[0]                # 4개이상 연속문자 체크
    check_i = 1                         # 몇개나 연속인지 체크
    check_ch = {inp_str[0]: 1}          # 5개이상 같은 문자포함 체크
    for ch_idx in range(1, len(inp_str)):
        if inp_str[ch_idx] == include:
            check_i += 1
            if check_i == 4:
                answer.append(4)
        else:
            include = inp_str[ch_idx]
            check_i = 1

        if inp_str[ch_idx] not in check_ch:
            check_ch[inp_str[ch_idx]] = 1
        else:
            check_ch[inp_str[ch_idx]] += 1
    for item in check_ch.keys():
        if 5 <= check_ch[item]:
            answer.append(5)

    # 규칙에 계속걸릴수있으니 set으로 한번 묶자
    temp_an = set(answer)
    answer = list(temp_an)
    if not answer:
        return [0]
    return answer