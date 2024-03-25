# 계좌 개설
# global을 활용한 자주 사용하는 매개변수 없애기
# 매개변수와 반환값이 있는 함수 선언

def OpenAccount(name):
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name


# 잔액과 입금액을 매개변수로 전달 받음
def Deposit(moneyInput):
    global balance
    print(f"{moneyInput}이 입금 되었습니다. 잔액은 {balance + moneyInput}입니다.")


def Withdraw(moneyInput):
    global balance
    if balance >= moneyInput:
        print(f"{moneyInput}이 출금 되었습니다. 잔액은 {balance - moneyInput}입니다.")
    else:
        print("출금이 실패했습니다.")


balance = 0
name = OpenAccount("곰도리 사육사")
Deposit(1000)
Withdraw(500)
print(f"{name}의 잔액은 {balance} 입니다.")
