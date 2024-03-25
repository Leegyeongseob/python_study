# 조건문과 반복문은 제어문이라고 하고, 이는 순차적인 흐름을 제어하는 목적으로 사용
# 파이썬의 조건문은 자바의 if문과 switch 문을 결합한 형태와 유사하며, 파이썬은 switch문 없음.
# 조건문의 수행은 들여쓰기로 구분하고 각각의 조건은 :으로 구분
num = int(input("정수를 입력 하세요 : "))

if num >= 100:
    print("입력값이 100보다 커요")
elif num <= 100:
    print("입력값이 100보다 작아요")
else:
    print("입력값이 100과 같아요")

season = input("지금 계절은? ")
if season == "spring":
    print("따뜻한 봄이 왔어요")
elif season == "summer":
    print("무더운 여름이 왔어요")
elif season == " fall" or season == "autumn":
    print("쓸쓸한 가을입니다.")
else:
    print("추운 겨울입니다.")

# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70 이상 C, 60이상 D, 나머지는 F

# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70 이상 C, 60이상 D, 나머지는 F
# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70 이상 C, 60이상 D, 나머지는 F
while True:
    kor, eng, math = map(int, input("국어, 영어, 수학 성적을 입력해주세요:").split())
    average = sum([kor, eng, math]) / 3
    if average >= 90:
        print("등급: A")
    else:
        if average >= 80:
            print("등급: B")
        else:
            if average >= 70:
                print("등급: C")
            else:
                if average >= 60:
                    print("등급: D")
                else:
                    print("등급: F")
    num = input("종료하시겠습니까? 예[0], 아니요[1]")
    if num == '0': break

# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70 이상 C, 60이상 D, 나머지는 F
# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70 이상 C, 60이상 D, 나머지는 F

while True:
    kor, eng, math = map(int, input("국어, 영어, 수학 성적을 입력해주세요:").split())
    average = sum([kor, eng, math]) / 3
    if average >= 90:
        print("등급: A")
    else:
        if average >= 80:
            print("등급: B")
        else:
            if average >= 70:
                print("등급: C")
            else:
                if average >= 60:
                    print("등급: D")
                else:
                    print("등급: F")
    num = input("종료하시겠습니까? 예[1], 아니요[0]")
    if num == '1': break


while True:
    score = list(map(int,input("국어 영어 수학 성적을 입력하세요:").split()))
    average = sum(score)/len(score)
    if average >=90: print("A")
    elif average >= 80: print("B")
    elif average >= 70: print("C")
    elif average >= 60: print("D")
    else: print("F")
    num = input("종료하시겠습니까? 예[1], 아니요[0]")
    if num == '1': break


