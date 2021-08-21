

def validateAddress(n, li):

    for i in range(n):

        #끊기
        s_ip = []
        if ':' in li[i]:
            s_ip = li[i].split(':')
        elif '.' in li[i]:
            v4_check = True
            s_ip = li[i].split('.')
            for ip_cell in s_ip:
                # 길이는 3보다 클 수 없음
                if len(ip_cell) > 3:
                    v4_check = False
                integer_ip = int(ip_cell)
                # 7보다 작을경우엔 줄여쓰기 허용. 8과 11은 8진수와 혼동으로 앞에 0이 올 수 없음
                if integer_ip >= 8:
                    if integer_ip == 8 and not len(ip_cell) == 1:
                        v4_check = False
                    elif integer_ip == 11 and not len(ip_cell) == 2:
                        v4_check = False
                    elif len(ip_cell) < 3:
                        v4_check = False
            if v4_check:
                print('IPv4')
            else:
                print('어느 것도 아니다')
        else:
            print('어느 것도 아니다')


# ipv4
# print(validateAddress(1,['007.008.009.011']))
print(validateAddress(5, ['121.18.109.20', '0.12.12.34', '121.234.12.12', '23.45.12.56', '0.1.2.3']))
#
# print(validateAddress(5, ['2001:0db8:0000:0000:0000:ff00:0042:8329',
#                           '2001:db8::ff00:42:8329',
#                           '0000:0000:0000:0000:0000:0000:0000:0001',
#                           ': ',
#                           '2001.db8:ff00:42.8329']))
