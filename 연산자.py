# 연산자란? 프로그램에서 계산을 위해서 사용(사칙, 대입, 비교, 관계(논리), 비트 연산 등이 있음.)
# 산술 연산 : + , - , * , /(나누기) , %(나머지) , //(몫), **(제곱 연산자)
# 파이썬은 증감 연산자가 없다. ++, --
i = 10
j = 3
print(i+j)
print(i**j)
print(f"{i / j:.2f}")   # 나누기
print(i // j)   # 몫
text = "Python"
print(text * 3)

tax_rate = 0.10 #세율
income = int(input("당신의 수입은 얼마 입니까? : "))
print(f"당신이 내야 할 세금은 {income*tax_rate:.2f}입니다.")

# 관계(논리)연산자

x = 10
y = 20
z = 30

rst1 = x > 0 and x > y # &&, 둘다 참이어야 참, 거짓
rst2 = x > 0 or x > y # ||, 둘 중 하나만 참이면 참, 참
rst3 = not(x > 0 or x > y) # !, 참이면 거짓, 거짓이면 참, 거짓
print(rst1,rst2,rst3)


# 3항 연산자 (java ? 참 : 거짓) : 참과 거짓의 결과를 원하는 값으로 만들고 싶을 때 사용
# 파이썬 (조건식) and 참인 경우 수행 or 거짓인 경우 수행
age = int(input("나이를 입력: "))

adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {adult}입니다.")
num = int(input("정수 입력 : "))
is_even = num % 2 == 0 and "짝수" or "홀수"
print(f"{num}은 {is_even}입니다.")

print(42 == 0b101010) #b는 binary의 약어
print(42 == 0o52) #o는 octat 8진수를 의미
print(42 == 0x2a) #x는 haxsa 16진수를 의미
print(bin(42))
print(oct(42))
print(hex(42))

# 비트 연산자
a = 10
b = 12

print(a & b) #둘 다 1이어야 1,8
print(a | b) # 둘 중 하나만 1이면
print(a ^ b) # 값이 다른 경우 1,
print(~a) # 비트 반전, 음수 표기는 2의 보수로 표기하기 때문에 1이 모자람
print(a << 1) # 주어진 값 만큼 왼쪽으로 비트 이동, 20
print(a >> 1) # 5