# 튜플 : 값을 변경 할 수 없는(imutable) 시퀀스 자료형
# () 소괄호 사용해서 만들거나 괄호가 없으면 튜플
x = 10
y = 20,  # 언패킹
print(type(x))
print(y)

person = "Alice", 30, '곰돌이사육사', True  # Packing
print(person)

a, b, c, d = person  # Unpacking


# 튜플을 이용한 함수 반환 값 다루기
def get_person():
    name = "곰돌이 사육사"
    age = 25
    addr = "경기도 이천시"
    return name, age, addr

nameCard = get_person()
print(nameCard)
