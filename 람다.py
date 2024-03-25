# 람다(lamda)? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것
# 람다는 주로 이름없는 함수를 만든 때 사용
# 람다 장점은 코드의 간결함, 메모리 절약 등의 이점이 있음.
def Add(a, b):
    return a + b


print(Add(10, 20))
print((lambda a, b: a + b), (10, 20))


# 함수의 매개변수로 함수 전달하기

def CallTimes(func):
    for i in range(10):
        func()


def PrintHello():
    print("Hello!!")


# CallTimes(PrintHello)


def Power(n):
    return n * n


power2 = lambda n: n * n  # 람다식

# 와후!
inputNum = map(int, input("숫자를 입력해주세요 : ").split())
rst = list(map(lambda n: n * n , inputNum))
print(rst)
