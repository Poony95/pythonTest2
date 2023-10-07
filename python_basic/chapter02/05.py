# Chapter 03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형( 순서x, 키 중복x, 수정o, 삭제o)

# 선언 ( dict : key, value)
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '950209'}
b = { 0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}

e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade',  'A'),
    ('Status', True)
])


# 이렇게 사용하면 가장 가독성도 좋고 편하고 좋습니다!
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력 (get)
# print('a - ', a['name']) -> 존재 X - > 에러 발생
print('a - ', a.get('name')) # -> 존재 X - > None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City')) # f -  Seoul
print('f - ', f.get('Age')) # f -  33


# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

#딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

# items 는 튜플형태로 포함 되어 출력됨.
print('a - ', a.items()) # a -  dict_items([('name', 'Kim'), ('phone', '01033337777'), ('birth', '950209'), ('adress', 'seoul'), ('rank', [1, 2, 3])])
print('b - ', b.items())
print('c - ', c.items())
print('a - ', list(a.items())) # a -  [('name', 'Kim'), ('phone', '01033337777'), ('birth', '950209'), ('adress', 'seoul'), ('rank', [1, 2, 3])]
print('b - ', list(b.items()))


# pop 사용 시 원본에 있던 데이터는 삭제가 됩니다. 
print('a - ', a.pop('name')) # a -  Kim
print('a - ', a) # a -  {'phone': '01033337777', 'birth': '950209', 'adress': 'seoul', 'rank': [1, 2, 3]}

print('c - ', c.pop('arr'))
print('c - ', c)

print()
# popitem은 랜덤으로 값을 꺼내오는 것 why ? dictionary 는 순서 상관없기 때문에 '랜덤'값을 꺼내올 때 사용 하면 됩니다.
print('f - ', f.popitem())
print('f - ', f.popitem())

print()

# 키를 포함하고 있는지 확인하는 방법
print('a - ', 'birth2' in a) # a -  False  -> a 안에 birth2가 있어?

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='960202')
print('a - ', a)

temp = {'address':'Busan'}
a.update(temp)
print('a - ', a)