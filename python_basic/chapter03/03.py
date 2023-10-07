# Chapter03-03
# 파이썬 반복문
# While 실습

# while <expr>:
#   <statement(s)>

# 예제1

n = 5
while n > 0:
    print(n)
    n = n - 1


# 예제2

a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# 예제3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop end!")
print()


# 예제 4

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print("Loop end!")

# 예제 5
# if 중첩
i = 1

while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# while - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'baz'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
    print('i:',i)
else:
    print(s, 'not found in list.')

# 무한반복
# while Ture:
#   print('Foo')

# 예제8
a = ['foo', 'bar', 'baz', 'qux']

while True:
    if not a:
        break
    print(a.pop())