print(38)
print("문자열")
print([1, 2, 3])
print("파" + "이" + "썬")
print("파""이""썬") # 파이썬에서는 '" 모두 문자열로 간주
print("파", "이", "썬") #콤마는 구분자를 의미
print("\n\n\n") # \n 줄바꿈 문자를 의미
print("""
물론입니다! 점심으로 즐길 만한 몇 가지 추천 메뉴를 소개해 드리겠습니다:

샐러드 바: 건강한 식사를 선호하신다면 샐러드 바에서 신선한 채소와 과일, 단백질 소스를 곁들인 샐러드를 즐기는 것도 좋은 선택입니다.
샌드위치: 다양한 종류의 샌드위치 중에서 마음에 드는 한 가지를 선택하여 즐겨보세요. 터키 샌드위치, 치킨 샐러드 샌드위치, 혹은 베지테리언 옵션 등 다양한 선택이 가능합니다.
라면 또는 국수: 간단하면서도 포만감을 주는 라면이나 국수도 좋은 선택입니다. 다양한 종류의 라면 또는 국수 중에서 자신이 좋아하는 종류를 골라 즐겨보세요.
햄버거: 분식류 중에서 햄버거를 즐기는 것도 좋은 방법입니다. 다양한 토핑과 소스로 맛을 낼 수 있으며, 곁들일 감자튀김이나 사이드 메뉴도 함께 즐길 수 있습니다.
중식 뷔페: 중식 뷔페나 중국 요리집에서 다양한 종류의 차이나 요리를 즐길 수도 있습니다. 탕수육, 짬뽕, 볶음밥 등 다양한 메뉴를 맛볼 수 있습니다.
위의 메뉴들 중에서 원하는 것을 선택하여 즐기시길 바랍니다! 만약 특정 식당이나 요리 종류에 대한 추가 정보가 필요하시면 언제든지 물어주세요.
""")
print("안녕하세요. 라고 \"곰돌이 사육사\"가 말했습니다.")
print('안녕하세요. 라고 "곰돌이 사육사"가 말했습니다.')
print("서울시\t강남구\t역삼동")
print("사과\r바나나") # 캐리지 리턴

# end : 출력 할 때 가장 마지막에 자동으로 삽입되는 문자 지정 옵션(기본이 줄바꿈)
# sep : 중간에 삽입되는 문자를 지정하는 옵션(기본이 공백 한칸)
print("Hello", end="")
print("Hellow안녕하세여world",sep="안녕하세여")
print('010','8603','3487',sep="-")
year = 2024
month = 3
day = 19
print(year,month,day,sep="/")

name = "곰돌이 사육사"
age = 22
gender = '남성'
jobs = "소프트웨어 개발자"
addr = "경기도 수원시"
# c언어 스타일, %방식(서직을 지정하는 방식) = printf
print("="*5 ,"스타일 지정방식","="*5,sep="")
print("이름 : %s" %name)
print("나이 : %d , 성별 : %s" %(age,gender))
print("주소 : %s"%addr)
# old스타일 python 3.6이전 스타일
print("="*5 ,"python 3.6이전 스타일","="*5,sep="")
print("이름 : {} 주소 : {}".format(name,addr))
print("나이 : {0}".format(age))
# 파이썬 현재 스타일
print("="*5,"python 현재 스타일","="*5,sep="") # f-print 방식
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {jobs}")
print(f"주소 : {addr}")
# 자바 스타일 : + 연산자 사용
print("======자바스타일======")
print("이름 : "+name)
print("나이 : "+str(age))
print("성별 : "+gender)
print("직업 : "+jobs)
print("주소 : "+addr)

#출력시 정렬
# < - 좌측 정렬
# > - 우측 정렬
# ^ - 중앙 정렬

number = 125
pi = 3.14159265478987
print(f"|{number:6}|") # 5칸의 공간을 만들고 값을 오른쪽 정렬
print(f"|{number:<6}|") #5칸의 공간을 만들고 값을 왼쪽 정렬
print(f"|{number:^6}|") #5칸의 공간을 만들고 중앙 정렬
print(f"{pi:.2f}") #실수값을 소수점 3번째 자리에서 반올람해서 소수점 이하 2자리 출력




