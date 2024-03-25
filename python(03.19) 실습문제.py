### [실습문제] 세자리수 중에서 가장 큰 수
# - 3자의 정수를 입력을 받아 100의자리, 10자리, 1의 자리로 나누어 담고 가장 큰수를 찾아서 출력
# - 예) 입력 : 574, 출력 : 7

num = int(input("세자리수를 입력하세요:"))
hundred = num//100
ten = (num % 100)//10
one = num % 10
print(max([hundred, ten, one]))


### [실습문제] 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간근무 : 주간 시급 * 1.5

chi = input("주간근무[1], 야간근무[2]를 입력 하세요 : ")
work_time = int(input("근무시간을 입력해 주세요:"))
if chi == 1: salary = work_time*9620
else: salary = work_time*9620*1.5
print(f"{work_time}시간 동안 근무한 주간 또는 야간 급여는 {(int)(salary):,}원입니다.")



# work_list = list(map(int,input("주간,야간 근무 시간을 입력해 주세요. : ").split()))
# print(f"아르바이트 급여 : {(int)(work_list[0]*9620+work_list[1]*9620*1.5):,}원")

