# 3개의 정수를 입력 받아 최대값 / 최소값 구하기
# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# 2개의 문자열을 변수 s와 k에, 양의 정수를 변수 n에 각각 전달 받아
# s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
#
# 문제 1. 3개의 정수를 입력 받아 최대값/ 최소값 구하기

num1,num2,num3 = map(int,input("3개의 정수를 입력해 주세요:").split())
print(max(num1,num2,num3))  #최대값
print(min(num1,num2,num3))  #최소값

# 2. 주민등록번호를 입력받으면 생년월일, 성별, 나이 출력하기
from datetime import datetime
current_year = datetime.today().year # 현재 시간을 출력

while True:
    ID_num = input("-를 포함하여 주민등록번호를 입력해 주세요(종료[0]): ")
    #반복문을 빠져 나가는 부분
    if ID_num =='0': break
    ID_num_list = ID_num.split("-")
    std = ID_num_list[1][0] #기준이 되는 부분(주민등록번호 뒷자리의 첫번째 자리)
    #생년월일을 출력하는 부분
    #1800~1899년 출생
    if std == '0' or std =='9':
        print(f"생년월일 : 18{ID_num_list[0][0:2]}년 {ID_num_list[0][2:4]}월 {ID_num_list[0][4:]}일")
        #나이도 같이 계산
        age = current_year - (int(ID_num_list[0][0:2])+1800)
    #1900~1999년 출생
    elif std == '1' or std =='2':
        print(f"생년월일 : 19{ID_num_list[0][0:2]}년 {ID_num_list[0][2:4]}월 {ID_num_list[0][4:]}일")
        #나이도 같이 계산
        age = current_year - (int(ID_num_list[0][0:2])+1900)
    #2000년 이후 출생
    elif std == '3' or std =='4':
        print(f"생년월일 : 20{ID_num_list[0][0:2]}년 {ID_num_list[0][2:4]}월 {ID_num_list[0][4:]}일")
        #나이도 같이 계산
        age = current_year - (int(ID_num_list[0][0:2])+2000)
    else:
        print("잘못된 주민번호입니다. 다시 입력해주세요.")
        break
    # 성별을 출력하는 부분
    if std == '9' or std == '1' or std =='3': print("성별 : 남자")
    elif std == '0' or std == '2' or std =='4': print("성별 : 여자")
    else:
        print("잘못된 주민번호입니다. 다시 입력해주세요.")
        break
    #나이를 출력하는 부분
    print(f"나이 : {age}세")

# # 문제 3. 2개의 문자열을 변수 s와 k에, 양의 정수를 변수 n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
s,k,n = input("두개의 문자열과 하나의 숫자를 입력하세요:").split()
print(f"{s[-int(n):]}{k}")


# 여러개의 정수를 입력 받아 합계와 평균 구하기

num2 = list(map(int,input("정수 여러개 :").split()))
print(f"합계 : {sum(num2)}")
print(f"평균 : {sum(num2)/len(num2)}")