# 파이썬 완전 기초 
# chapter 01-3
# 파이썬 변수

# 기본 선언
n = 700

print(n * 700)

# 출력
print(n)
print(type(n))

# 동시선언
x = y = z = 700
print(x,y,z)


# 선언
var = 75
# 재선언
var = "change value"

# 출력
print(var)
print(type(var))

# object references
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)


# 예2)
#  n -> 777
n = 777
print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id (identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트를 참조함 ( 다른 변수명에 있어도 값이 같다면 파이썬은 알아서 하나의 오브젝트로 인식하고 사용함. -why? 파이썬 interpreter 가 그렇게 만들어져있음)
"""
2027609046928
2027609046928
True
"""

m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel case : numberOfCollegeGraduates -> Method ( 맨 앞글자 소문자 이후 철자 앞 대문자 )
# Pascal case : NumberOfCollegeGraduates -> Class ( 맨 앞글자 대문자 이후 철자 앞 대문자 )
# Snake Case : number_of_college_graduates -> 파이썬 변수에 사용 많이 함

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
# 그러나 카멜 혹은 스네이크 기법으로 변수명 사용하기

# 예약어는 변수명으로 불가능 ( as, class, and, assert, if, elif ...)

