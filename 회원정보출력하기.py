#
# name = input("이름 입력: ")
# jobs = ["학생","회사원","주부","무직"]
# age = int(input("나이입력(1~199): "))
# if age < 1 or age > 199:
#     age = int(input("다시 입력해주세요. :"))
# gender = input("성별입력(남자:m,M 여자:F,f): ")
# gender = gender.upper()
# if gender == "M":
#     gender = "남성"
# elif gender == "F":
#     gender = "여성"
# else:
#     gender = input("다시 입력해주세요. :")
# job = int(input(f"1({jobs[0]}),2({jobs[1]}),3({jobs[2]}),4({jobs[3]}):"))
# if job < 1 or job > 4:
#     job = int(input("다시 입력해주세요. :"))
# print(f"이름:{name} 나이:{age}세 성별:{gender} 직업:{jobs[job-1]}")

##역할별로 함수 만들기

# 회원 정보 출력 하기 (1단계는 현재 상태대로 -> 함수 형태로)
def input_age() :
    while True :
        age = input("나이를 입력하세요 : ")
        if age.isdigit():  # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200: return age
        print("나이를 잘못 입력하셨습니다.")

def input_gender() :
    while True :
        gender = input("성별을 입력하세요 : ")
        if gender == 'M' or gender == 'm' : return "남성"
        elif gender == 'F' or gender == 'f' : return "여성"
        print("성별이 잘못 입력되었습니다.")

def input_jobs() :
    while True :
        jobs = input("직업을 입력하세요 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘못 입력하셨습니다.")

def print_info(name,age,gender,jobs):
    jobs_str = "", "학생", "회사원", "주부" ,"무직" #튜플
    print("="*3, "회원정보", "="*3)
    return f"이름: {name}\n 나이: {age}\n 성별: {gender}\n 직업: {jobs_str[jobs]}"

#함수 호출과 파일 저장하기
fd = open("member.txt", 'wt', encoding="UTF-8")
while True:
    name = input("이름 입력 / 종료는 quit : ")
    if name == "quit": break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name,age,gender,jobs)
    fd.write(rst + '\n')
fd.close()