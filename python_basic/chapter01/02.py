

# 파이썬 완전 기초 
# chapter 01-2
# 파이썬 3가지 Print Formatting

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력 1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y))
print(ex1)

# 출력 2
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력 3 (f string 사용법 : '' 앞에 f 라고 작성 후 이어서 사용해주면 됩니다.) 출력 -> n = Lee, s = 308276567, sum=150
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)

# 구분기호 (화폐관련 표시 할 때 사용) 출력 -> m : 100,000,000
m = 100000000 
print(f'm : {m:,}')

print()
print()

# 정렬
# ^ : 가운데, < : 왼쪽 , > : 오른쪽

t = 20

print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")


print()
print()

# 정렬 기호 앞에 문자 넣으면 공백을 그 문자로 채울 수 있습니다.
print(f"t center : {t:-^10}")
print(f"t center : {t:#^10}")


