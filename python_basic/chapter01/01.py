# 파이썬 완전 기초 
# chapter 01-1

# 기본 출력
print('python start!')
print("python start!")
print('''python start!''')
print("""python start!""")

print()

# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep=' ')
print('010', '1234', '5678', sep='-')
print('python', 'google.com', sep='@')

print()

#end 옵션
print('welcom to', end='  ')
print('IT news', end='  ')
print('web site')
print()

# file 옵션
import sys
print('Learn python', file=sys.stdout)
print()

#format 사용 (d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))  # 인덱스 순서를 바꿔서 출력이 거꾸로 됨.
print()


#%d = decimal, %s = string, %f = float

# %s (문자열 출력 시 %s)
# 왼쪽 공백
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
# 오른쪽 공백
print('%-10s' % ('nice')) 
print('{:10}'.format('nice'))
# 원하는 문자(*, @ ...)로 채운 후 출력
print('{:*>10}'.format('nice'))
# 중간 정렬 후 출력 -> ^
print('{:^10}'.format('nice'))
# 앞에서부터 n개의 글자만 절삭하고 출력하고 싶은 경우 ('%.5s', '{:10.5}')
print('%.5s' %  ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()

# %d ( 정수인 경우 %d 로 출력해야 함)
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f ( 실수형 출력 )
print('%f' % (3.14213515321532))
print('{:f}'.format(3.123151532))

# 절삭형 (실수 출력)
print('%1.8f' % (3.143131312315321))
# 03.143 -> 아래의 경우에는 총 출력 6개 자리수 중 한 개만 정수이기 때문에 앞에 숫자 하나는 0으로 채운 것 !! 어렵
print('%06.3f' % (3.1431315321))
print('{:06.3f}'.format(3.142313513))

