# chapter08-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가모드 a, 텍스트모드 : t, 바이너리 모드 : b
# 상대 경로 : ('../, ./'), 절대 경로 ( 'c:\Django\exmple..)

# 절대경로는 처음부터 다 적어줘야 하는 단점이 있음
# f = open('C:\\pythonTest\\source_code\\resource\\it_news.txt')

# 상대경로
f = open('./resource/it_news.txt', 'r', encoding='utf-8')
#  속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 반드시 close
f.close()

# 예제2
# with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
#     c = f.read()
#     print(c)
#     print(iter(c))
#     print(list(c))

# print()

# 예제 3
# read() : 전체 읽기, read(10), 10Byte (중요)
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)  # 파이썬이 이전에 끝난 문장을 기억하고 있어서 맨앞으로 갈 땐 seek 사용합니다.
    c = f.read(20)
    print(c)

print()

# 예제 4
# readLine :  한 줄, 한 줄 읽어오게 할 때 
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)

print()


# 예제 5
# readLines :  전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()



# 파일 쓰기 (write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:   # w 는 write 로  정보 추가하는 것
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:   # a 는 append 로 기존의 정보에 추가하는 것
    f.write('I love python\n')

# 예제3
# writeLines: 리스트를 -> 파일로 (중요)
with open('./resource/contents2.txt', 'w') as f:  
    list = ['Oranges\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
    
# 예제4
with open ('./resource/contents3.txt', 'w') as f:  
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)