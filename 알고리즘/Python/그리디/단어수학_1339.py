import sys

from collections import Counter

if __name__ == "__main__":
    ''' 
    문자열 길이순 정렬 후 최빈값을 배열에 저장
    '''

    n = int(sys.stdin.readline())
    m_len = 0
    words = {'9': '', '8': '', '7': ''}
    for _ in range(n):
        w = sys.stdin.readline()
        words.append(w)
        if len(w) > m_len:
            m_len = len(w)

    w_c = [[] for _ in range(0, m_len)]
    for w in words:
        for i, ch in enumerate(w):
            w_c[i].append(ch)

    m_num = 9
    dicn = {''}
    for ws in w_c:
        cnt = Counter(ws).most_common()
        for i,item in enumerate(cnt):
            dicn[item[i]] = m_num
            m_num -= 1

    print(dicn)

