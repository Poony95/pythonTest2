#  Chapter07-1
# 파이썬 내장(Built- in) 함수
#  자주 사용하는 함수 위주로 실습
# 사용하다 보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()

print(abs(-3))

# all : iterable 요소 검사( 참, 거짓 )
print(all([1,2,''])) # and  
print(any([1,2,0])) # or

# chr : 아스키 -> 문자
# ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + Iterable 객체 생성
for i , name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)
'''
1 abc
2 bcd
3 efg
'''

# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

# 함수 선언 하고 사용하는 방식 
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6]))) 

# 람다 방식으로 한 번 사용시에 간단한 코드로 구현한 방식
print(list(filter(lambda x : abs(x) > 2, [1, -3, 2, 0, -5, 6])))

#  id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# led : 요소의 길이 반환
print(len('abvdefg'))
print(len([1,2,3,4,5,6]))

# max, min : 촤대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,  [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x : abs(x),  [1, -3, 2, 0, -5, 6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(6.5781, 2))

# sorted : 반복가능한 객체(Iterable) ( 순서대로 오름차순 정렬하여 반환 )
print(sorted([6,7,4,3,5,1]))
print(sorted(['p','y','t','h','o','n']))

# sum : 반복가능한 객체 합 반환
print(sum([6,7,8,9,710]))
print(sum(range(1,101)))

# type: 자료형 확인
print(type(2))
print(type({}))
print(type([]))

# zip : 반복가능한 객체의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50]))) # 짝이 이루어지지 않는경우 데이터 출력 x


