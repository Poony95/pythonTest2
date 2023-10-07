#chapter05-2_ex1
# 파이썬 사용자 입력
# input 사용법 (2023 추가)
# 기본 타입 (str)

# 예제1 -> 예외처리
# try:
#     n = int(input('Enter a number : '))
#     print('ok, your number is : ', n)
# except ValueError:
#     print('This is not a number.')

# 예제2 -> 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input('Enter a number : '))
        break
    except ValueError:
        print('THis is not a number')

print('OK, your number is : ', n)