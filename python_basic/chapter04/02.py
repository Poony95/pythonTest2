#chapter05-2
# 파이썬 사용자 입력
# input 사용법
# 기본 타입 (str)

# 예제1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company : ")

print(name, grade, company)


# # 예제2
number = input("Enter number :")
name = input("enter name : ")

print("type of number", type(number), number * 3)
print("type of name", type(name))

# 예제 3 ( 계산 )
first_number = int(input("enter number1 : "))
second_number = int(input("enter number2 : "))

total = first_number + second_number
print('합 : ', total)

# 예제 4
float_number = float(input("Enter a float number : "))

print("input float : ", float_number * 1.213)
print("input type : ", type(float_number))

# 예제 5
print("FirstName - {0}, LastName - {1}".format(input("Enter First name : "), input("Enter second name : ")))