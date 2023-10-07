# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형( 순서, 중복, 수정, 삭제 허용)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
print(len(c)) # String도 시퀀스형이기 때문에 똑같이 len을 사용할 수 있는 것 
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d -', d[1])
print('d -', d[0] +d[1] +d[1])
print('d -', d[-1])
print('e -', e[-1][1]) # 중첩 이중문 같은 경우 [이중문의 위치], [몇번째 값]
print('e -', list(e[-1][1]))  # e - ['B', 'a', 's', 'e'] --> 앞에 list 라고 넣으면 단어를 분해하여 list 형태로 만들어줌

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:]) # d -  ['Ace', 'Base', 'Captine']
print('e - ', e[-1][1:3]) # e -  ['Base', 'Captine']

# 리스트 연산
print('>>>>>')
print('c + d ', c+d) # 리스트 + 리스트 = 리스트
print('c * 3', c * 3) # c 리스트가 세번 나옵니다.
print("'Test' + c[0]", 'Test' + str(c[0])) #'Test' + c[0],  Test70
print()

# 값 비교
print(c == c[:3] + c[3:]) # 70, 75, 80 +  85
print(c)
print(c[:3] + c[3:])
print()

# Identity(id) -> 리스트도 변수 안의 리스트 값이 같으니까 같은 id 를 사용함. 즉, 하나의 temp의 변수값이 바뀌면 c도 같이 바뀜
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제 
print('>>>>>')
c[0] = 4
print('c - ', c)
# 리스트 추가 시 두 개의 차이 알기!
c[1:2] = ['a', 'b', 'c'] #  c -  [4, 'a', 'b', 'c', 'b', 'c', 80, 85] ->  슬라이싱의 경우 : 중첩 이중문이 아님
print(' c - ', c)
c[1] = ['a', 'b', 'c'] #  c -  [4, ['a', 'b', 'c'], 'b', 'c', 80, 85] ->  슬라이싱이 아닌 경우 : 중첩 이중문
print(' c - ', c)

print()

c[1:2] = [] # 삭제1
print(' c - ', c)
del c[2] #삭제2
print('c - ',c)

#리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 마지막에 해당 숫자 추가해라
print('a - ', a)
a.sort() # sort로 오름차순 정렬
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3]) # 두개 다 같은 것
a.insert(2,7) # insert : 추가할 위치, 값
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[9543]
a.remove(10)  # 불필요한 데이터를 리스트에서 제거 하고자 할 때에는 remove 함수를 사용합니다.
print('a - ', a)
print('a - ', a.pop())  # pop 이라는 함수는 가장 마지막에 작성 된 글을 꺼내올 때 사용합니다 . ( 마지막에 올린 맨 위의 접시를 빼는 것 처럼 )
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))   # a 안에 4가 몇개 있는가??

ex = [8,9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del 

# 반복문 활용
while a:
    data = a.pop()
    print(data)

print('a - ', a) # a -  []





