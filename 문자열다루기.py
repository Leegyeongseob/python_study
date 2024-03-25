a_str = "Hello Python Program"
new_str2 = a_str.replace("Python", "JavaScript")
print(new_str2)
# 문자열에 포함된 문자 갯수 세기(count()), 문자열 길이(len(), __len__())
print(a_str.count("l")) # 해당 문자열에서 count()함수에 전달 문자가 몇개 존재하는 반환
print(len(a_str)) # 문자열 길이를 반환하는 함수
print(a_str.__len__()) #문자열 길이를 반환하는 함수
# 문자열 찾기 : find()찾은 문자열 인덱스 변환, 없으면 -1,
# rfind() : 뒤에서부터 문자열을 찾고 찾은 인덱스는 앞에서 계산
# index() 찾은 문자열의 인덱스 반환, 없으면 ValueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("나에게"))
# print(phrase.index("나에게")) # 없어서 에러 발생 valueError
new_str = phrase.replace("가장","나에게")
print(new_str)
# 분자열 연산자 : "문자열" + "문자열", "문자열"*3
print("눈물의"+"여왕")
print("등업"*3)
print("집가고 싶다\n")
# 문자열 양옆의 공백 제거 : strip()
input_a = """

        안녕하세요.
문자열 함수를 알아 봅니다.


"""
print(input_a.strip())