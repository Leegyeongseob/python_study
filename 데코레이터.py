# 이미 만들어져 있는 함수의 앞과 뒤에 기능을 추가 할 때 사용됨.
# 스프링부트에서는 AOP(Aspect, Oriented, Program)이라고 부름.
from datetime import datetime as dt


def DatatimeDeco(func):
    def Decorated():
        print(dt.now())
        func()
        print(dt.now())

    return Decorated


@DatatimeDeco # 안쪽 핵심함수
def ForSum():
    sum = 0
    for i in range(1, 10000000):
        sum += i
    print(sum)


ForSum()
