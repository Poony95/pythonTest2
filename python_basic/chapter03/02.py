# chapter03-02
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10):        # 0 ~ 9
    print('v1 is : ', v1)

for v2 in range(1, 11):     # 1 ~ 10
    print('v2 is : ', v2)

for v3 in range(1, 11, 2):     # 1 ~ 10 , + 2 단위로 (짝수, 홀수 만들기)
    print('v3 is : ', v3)   


# 1 ~ 1000 합
sum1 = 0

for v4 in range(1, 1001):
    sum1 += v4
print('1 ~ 1000 Sum : ', sum1)

# 1~ 1000 까지 3의 배수의 합을 구하기 (3부터 시작)
print('1 ~ 1000 까지 3의 배수 합 : ', sum(range(3, 1001, 3))) 


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

#예제
names = ['Kim','Park','Cho','Lee','Choi','Yoo']

for n in names:
    print(' You are : ', n)


# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("current Numbers :", n)

# 예제 3
word = "Beautiful"

for s in word:
    print('word : ', s)

# 예제 4
my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "City" : 'Seoul'
}

# 예제 5 ( key, value 값 for문으로 가져오기)
for key in my_info.keys():
    print('key : ', key)

for v in my_info.values():
    print(' values : ', v)


# 예제 5 ( 대문자, 소문자로 출력하기)

name = 'PineApple'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
'''
P
I
N
E
A
P
P
L
E
'''

# break (if 문에서 어떠한 조건에 부합하면 끝까지 가는 것이아니라 break 시킴)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("found : 34!")
        break
    else:
        print("not Found : ", num)

# continue ( if 조건문에서 건너 뛰고 싶은 Type(타입)을 건너 뛰고 다른 타입만 나타내고 싶을 때 countinue 사용 )

lt = ["1",  2, 6, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : " , v, type(v))

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("found : 24")
        break
    else:
        print('not found: 24')
else:
    print('error')


# 구구단 출력하기 

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제

name2 = 'Aceman'

print('Reversed', reversed(name2))
print("list", list(reversed(name2)))
print("Tuple", tuple(reversed(name2)))
print("set", set(reversed(name2)))