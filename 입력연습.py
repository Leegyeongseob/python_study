# 사용자의 입력을 처리하는 input() 함수, 기본값은 문자열로 입력 됨
name = input("이름을 입력 하세요 : ")
print(name)
age = int(input("나이를 입력하세요 : "))
print(age)

#map을 이용하여 split으로 자른 여러개의 인자 값을 가공하여 반환
# map(callback함수(변환해줄 자료형),변환할 값들)
kor, eng, mat = map(int, input("국어 영어 수학 : ").split())
print(f"국어 :{kor}, 영어 : {eng}, 수학 : {mat}")


name, addr = input("이름과 주소 입력: ").split() #문자열을 split 기준으로 입력(튜플의 특성)
print(f"이름 : {name} , 주소 : {addr}")

# 입력 제한 없이 다 받고 싶은 경우
score = list(input("성적을 마음대로 입력해주세요 : ").split())
print(f"""성적 리스트 :
{score}""")

# split 활용

hour, min, sec = input("시:분:초").split(":")
print(f"{hour}시 {min}분 {sec}초")

hour, min, sec = map(int,input("시:분:초 ").split(":"))
if(hour > 12):
    hour -= 12
    print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
else:
    print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")
