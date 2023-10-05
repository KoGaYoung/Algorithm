import sys

if __name__ == "__main__":
    '''
    단순히 숫자가 적은걸로 판별하는 것이 아닌
    뭉탱이 갯수가 적은것을 골라야한다.
    0001100
    '''
    s = input()
    s1 = s.split('0')
    s2 = s.split('1')

    s1_c = 0
    s2_c = 0
    for i in s1:
        if i != '':
            s1_c += 1

    for i in s2:
        if i != '':
            s2_c += 1
    print(min(s1_c, s2_c))