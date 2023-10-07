# Chapter 03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서ㅇ, 중복ㅇ, 수정x, 삭제x) # 불변 -> 중요한 정보,, 절대 변하지 않아야 할 값들을 저장할 때 필요함.

# 선언

a = ()
b = (1)
c = (11,12,13,14)
d = (100,1000, 'Ace', 'Base', 'Captine')
e = (100,1000, ('Ace', 'Base', 'Captine'))

print(type(a), type(b)) # <class 'tuple'> <class 'int'>


# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1]) # e -  ('Ace', 'Base', 'Captine')
print('e - ', e[-1][1]) # e -  Base
print('e - ', list(e[-1][1])) # e -  ['B', 'a', 's', 'e']

# 수정 xxx
# d[0] = 1500 
# #TypeError: 'tuple' object does not support item assignment

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3]) # d -  ('Base', 'Captine')

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)


# 튜플 연산
a = (5, 2, 3, 1, 4) # 튜플 
b = [5, 2, 3, 1, 4] # 리스트 
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹

# 팩킹
t = ('foo', 'bar', 'bax', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹
(x1, x2, x3, x4) = t

print(type(x1),type(x2),type(x3),type(x4))
print(x1, x2, x3, x4)

# 팩킹은 괄호가 있든 없든 튜플임
a = (1, 2, 3)
a = 1, 2, 3
