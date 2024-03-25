#for문은 정해진 범위 만큼 반복 할 때 주로 사용
#for 요소 in 시퀀스: 시퀀스는 리스트, 튜플, 문자열 등을 의미, 자바의 향상된 for와 유사
fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
for e in fruits:
    print(e, end="")



#for 변수 in range(시작값, 종료값, 증감값): 자바의 일반적인 for문과 유사
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1): # 1부터 n까지
    sum +=i
print(sum)

# 이중 for문 사용하기

n = int(input("정수를 입력 : "))
for i in range(0,n):
    for j in range(0,n):
        if j % 2 == 0:
            print("*",end="")
        else:
            print("*",end="")