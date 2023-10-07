# chapter 02-2
# 문자형

# 문자열 생성

str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''thank you!'''

# 타입
print(type(str1),type(str2),type(str3),type(str4))
# 문자 개수
print(len(str1),len(str2),len(str3),len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용

"""
\n : 개행 
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
/000 : 널 문자
...

"""
# I'm Boy
print('I\'m Boy')
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String  -> r 파일 형식이지만 날 것 그대로 문자열 ( 이스케이프 문자를 사용하지 않기 위해 변수를 사용)
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력 ( ''' abc ''' 해주는데 = 옆에 '\' 역슬러시를 넣어주면 이 다음에 어떤 변수를 바인딩 하는구나라고 앎)
# 역슬러시 사용 ( \ )
multi_str = \
'''
Multi line
String
Test
'''
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple!"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # PythonPythonPython
print(str_o1 + str_o2) # PythonApple
print('y' in str_o1) # True  y 가 str_o1 안에 들어있니?
print('n' in str_o1) # True
print('P' not in str_o2) # True -> apple 의 p 는 소문자이기 때문에 (대소문자 구별)

# 문자열 형 변환
print(str(66),type(66))
print(str(10.1))
print(str(True), type(str(True))) # True, <class 'str'>

# 문자열 함수 ( upper, isalnum, startswich, count, endwith, isalpha...)

# 맨 앞글자 대문자로 변환 
print("Capitalize : ", str_o1.capitalize())
# 모든 문단 뒤에 어떠한 문자가 붙어 있어야하는데 잘 붙어있는지 확인할 때 
print("endswith : ", str_o2.endswith("!"))
print("replace :", str_o1.replace('thon', ' good')) # python ->  pygood 중요!!
print("sorted : ", sorted(str_o1)) # sort :  ['h', 'n', 'o', 'p', 't', 'y'] -> 정렬이 되어 나옵니다.
print("split : ", str_o4.split(' ')) # 특정 단어를 분리할 때 사용

# 반복 (시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # '__iter__' 가 있으면 반복할 수 있다는 뜻

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습 !! 중요
str_s1 = "Nice Python"

# 슬라이싱
print(str_s1[0:3]) # 0 1 2 -> Nic
print(str_s1[5:]) # [5:11] -> Python
print(str_s1[:len(str_s1)]) # [:11] -> Nice Python
print(str_s1[:len(str_s1)-1]) # [:10]
print(str_s1[1:9:2]) # 0~8 까지의 수를 가져오고 2단위로 뛰어넘은 문자만 출력해라 

# - 의 경우 뒤에서 부터 출력하는 것
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'
 
print(ord(a))
print(chr(122))



