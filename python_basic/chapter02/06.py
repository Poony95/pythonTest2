# Chapter 03-6
# 파이썬 집합(set) 특징
# 집합(set) 자료형(순서 x, 중복 x)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}  # key와 value 로 되어있지 않다면 dict 이 아니고 set에 해당됩니다.
f = {42, 'foo', (1, 2, 3), 3.141592}

print('a - ' , type(a), a)
print('b - ' , type(b), b)
print('c - ' , type(c), c)
print('d - ' , type(d), d)
print('e - ' , type(e), e)
print('f - ' , type(f), f)

# 튜플 변환 ( set -> tuple )
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환( set -> list )
l = list(c)
l2 = list(e)

print('l - ' , l)
print('l2 - ' , l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

# 합집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2', s1.union(s2))

# 차집합
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인 (중복된 값이 있다면 : false, 중복된 값이 없다면 : true )
print('s1 & s2', s1.isdisjoint(s2))

# 부분 집합 확인
print(s1.issubset(s2)) # ( s1 에 s2 가 포함되는 부분집합이 아니기 때문에 false)
print(s2.issuperset(s2)) # ( 반대로 s2 에 s1 가 포함되는 부분집합이 아니기 때문에 false)

# 추가 $ 제거
s1 = set([1,2,3,4])

s1.add(5)
print('s1 - ', s1)

# remove는 값이 없는 경우 error 발생, discard 는 에러 발생하지 않음
s1.remove(5)
print('s1 - ', s1)

s1.discard(4)
print('s1 - ', s1)

# 전부 싹 지우고 싶을 땐 clear()함수 사용
s1.clear()
print('s1 - ', s1)
