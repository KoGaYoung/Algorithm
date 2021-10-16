def solution(registered_list, new_id):
    '''
    S : 소문자(a~z) 문자열 길이는 3 ~ 6
    N : 숫자(0~9) 문자열 길이는 0 ~ 6 -> 비어있을수도 첫자리는0아님

    '''
    if new_id not in registered_list:
        return new_id
    else:
        c = 0
        len_id = len(new_id)
        while c < len_id and new_id[c].isalpha():
            c += 1
        s = new_id[:c]
        n = new_id[c:]

        n_n = 1 if n == '' else int(n) + 1
        while s + str(n_n) in registered_list:
            n_n += 1

    return s + str(n_n)

print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))  # "ace15"
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))  # "cow10"
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))  # "bird100"
print(solution(["apple1", "orange", "banana3"], "apple"))  # "apple"
