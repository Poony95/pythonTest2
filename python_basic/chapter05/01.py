# Chapter 05-1
# 파이썬 클래스
# OOP( 객체 지향 프로그래밍 ), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스의 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능 
# 인스턴스 변수 : 객체마다 별도 존재


# 클래스: 붕어빵 틀, 인스턴스: 붕어빵 틀을 가지고 찍어내는 객체(코드에서 사용하는 객체), 인스턴스란 객체에 포함됨
# Object(사물)을 구현할 대상을 객체라고 하며 설계도를 바탕으로 구성된 것을 인스턴스화라고 합니다.
# 클래스 : dog , 객체 : 강아지 속성에 따른 하나하나의 강아지, 인스턴스 : 설계도를 바탕으로 구성된 객체


# 예제1

class Dog: # object 상속
    # 클래스 속성
    species = "firstDog"

    # 초기화/ 인스턴스 속성 ( 자바에서 생성자 만드는 것과 같음 , 기본 생성자처럼 아무 조건 없는 경우에만 만들지 않아도 됨.)
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print('클래스 정보 : ', Dog)

# 인스턴스화 ( 인스턴스화 시킨 것의 값이 같더라도 다 다른 객체이다.)
a = Dog("mikky", 2)
b = Dog("kong", 9)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstDog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)


# 예제 2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() 예외

# func1은 매개변수가 없기 때문에 class를 호출 하고 메소드로 불러옴
SelfTest.func1()
# func2는 매개변수가 있기때문에 인스턴스(f)로 불러와서 사용
f.func2()
SelfTest.func2(f) # 이렇게도 사용 가능
# SelfTest.func2() # 매개변수 없이 사용은 안됨.. 예외


# 예제3 (재고관리)
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 
    stock_num = 0 # 재고

    def __init__(self, name):
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)

del user1
print('after', Warehouse.__dict__)



# 예제 4
class Dog: # object 상속
    # 클래스 속성
    species = "firstDog"

    # 초기화/ 인스턴스 속성 ( 자바에서 생성자 만드는 것과 같음 , 기본 생성자처럼 아무 조건 없는 경우에만 만들지 않아도 됨.)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('mong mong'))




