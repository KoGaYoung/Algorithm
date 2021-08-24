import sys
# if __name__ == "__main__":
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s =input()

for cro in a:
    s = s.replace(cro, ' ')

print(len(s))
# readline일경우 ln까지 한글자 더셈
#
# croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = input()
# for i in croa:
#     s = s.replace(i,' ')
# print(len(s))