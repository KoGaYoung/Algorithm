# 55-50+40

s = input()
s += ' '    # 원본 문자열에 공백 추가
s1 = ''     # 앞에 0을 없앤 계산식
buffer = '' # 임시 숫자 버퍼
for ch in s:
    if ch in ('-', '+', ' '):
        if buffer != '':
            s1 += str(int(buffer))
            buffer = ''
        s1 += ch if ch != ' ' else ''
    else:
        buffer += ch

data = s1.split('-')

sic = []

if len(data) >= 2:
    for idx, num in enumerate(data):
        sic.append(num)

        if idx == 0:
            sic.append('-(')
        elif idx == len(data)-1:
            sic.append(')')
        else:
            sic.append(')-(')

    st = ''.join(sic)
else:
    st = data[0]
print(eval(st))