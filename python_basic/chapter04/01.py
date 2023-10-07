#chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다

# 함수 정의 방법
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print('hello, ', w)

word = 'good boy'

first_func(word)

# 예제2
def return_func2(w1):
    Value = 'hello, ' + str(w1)
    return Value

x = return_func2('GoodBoy2')
print(x)


# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
x, y, z = func_mul(10)

print(x, y, z)


# 예제4(튜플리턴)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return(y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))

# 예제5(리스트리턴)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return[y1, y2, y3]

p = func_mul2(20)

print(type(p), p, set(p))

# 예제6(딕셔너리 리턴)
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return{'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul3(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs

# *args(언팩킹) -> 함수를 유연하게 사용할 떄 ( 매개변수를 정해 놓지 않고 사용할 때 언팩킹을 사용)
def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'park')
args_func('Lee', 'park', 'kim')

# **kwargs( 언팩킹 ) -> 함수를 유연하게 사용할 떄 ( 매개변수를 정해 놓고 사용할 때 언팩킹을 사용)
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1='lee')
kwargs_func(name1='lee', name2='kim')
kwargs_func(name1='lee', name2='kim', name3='park')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'lee', 'kim', 'park', age1=20, age=30, age3=40)

# 중첩함수 (부모 함수만 호출 가능, 자식 함수는 호출 할 수 없습니다.)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 100)

nested_func(100)

# func_in_func(100) 실행불가

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체를 생성 (이름이 있기 때문에)  -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20, 50))

lambda_mul_func = lambda x, y: x * y

print(lambda_mul_func(50 , 50))

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x, y:x * y)