sec = int(input())

s = ''
s += str(sec // 300)
sec %= 300

s += ' '
s += str(sec // 60)
sec %= 60

s += ' '

s += str(sec // 10)
sec %= 10

if sec != 0:
    print(-1)
else:
    print(s)
